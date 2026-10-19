from django.shortcuts import render, redirect
import joblib
import pandas as pd

from pathlib import Path
from django.conf import settings

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Prediction

from django.db.models import Count

# Create your views here.

BASE_DIR = Path(settings.BASE_DIR)

model = joblib.load(
    BASE_DIR / "predictor" / "titanic_model.pkl"
)

columns = joblib.load(
    BASE_DIR / "predictor" / "titanic_columns.pkl"
)


def home(request):
    result = None
    probability = None
    error = None

    if request.method == "POST":
        try:
            pclass = int(request.POST.get("pclass"))
            sex = int(request.POST.get("sex"))
            age = float(request.POST.get("age"))
            sibsp = int(request.POST.get("sibsp"))
            parch = int(request.POST.get("parch"))
            fare = float(request.POST.get("fare"))
            embarked = request.POST.get("embarked")

            # Input validation
            if pclass not in [1, 2, 3]:
                raise ValueError("Invalid passenger class.")

            if sex not in [0, 1]:
                raise ValueError("Invalid sex value.")

            if not 0 <= age <= 100:
                raise ValueError("Age must be between 0 and 100.")

            if sibsp < 0 or parch < 0 or fare < 0:
                raise ValueError("Values cannot be negative.")

            if embarked not in ["C", "Q", "S"]:
                raise ValueError("Please select a valid port.")

            # Prepare passenger data
            passenger = {
                "Pclass": pclass,
                "Sex": sex,
                "Age": age,
                "SibSp": sibsp,
                "Parch": parch,
                "Fare": fare,
                "Embarked_C": int(embarked == "C"),
                "Embarked_Q": int(embarked == "Q"),
                "Embarked_S": int(embarked == "S"),
            }

            input_data = pd.DataFrame(
                [passenger],
                columns=columns
            )

            # Predict survival
            prediction = model.predict(input_data)[0]

            probabilities = model.predict_proba(input_data)[0]
            probability = float(probabilities[1])

            if prediction == 1:
                result = "Survived"
            else:
                result = "Did Not Survive"

            # Save prediction for logged-in users
            if request.user.is_authenticated:
                Prediction.objects.create(
                    user=request.user,
                    passenger_class=pclass,
                    sex=str(sex),
                    age=age,
                    siblings_spouses=sibsp,
                    parents_children=parch,
                    fare=fare,
                    embarked=embarked,
                    prediction_result=int(prediction),
                    survival_probability=probability,
                )

        except (ValueError, TypeError):
            error = "Please enter valid passenger details."

    return render(
        request,
        "predictor/home.html",
        {
            "result": result,
            "probability": probability,
            "error": error,
        }
    )

def landing(request):
    return render(request, 'predictor/landing.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("dashboard")

    else:
        form = UserCreationForm()

    return render(request, "predictor/register.html", {
        "form": form
    })


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("landing")

    return redirect("dashboard")
@login_required
def dashboard(request):
    user_predictions = Prediction.objects.filter(
        user=request.user
    )

    total_predictions = user_predictions.count()

    survivors = user_predictions.filter(
        prediction_result=1
    ).count()

    non_survivors = user_predictions.filter(
        prediction_result=0
    ).count()

    context = {
        "total_predictions": total_predictions,
        "survivors": survivors,
        "non_survivors": non_survivors,
        "model_accuracy": 81.01,
    }

    return render(
        request,
        "predictor/dashboard.html",
        context
    )


@login_required
def prediction_history(request):
    predictions = Prediction.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "predictor/history.html",
        {"predictions": predictions}
    )

@login_required
def analytics(request):
    predictions = Prediction.objects.filter(user=request.user)

    # Survival summary
    survivors = predictions.filter(
        prediction_result=1
    ).count()

    non_survivors = predictions.filter(
        prediction_result=0
    ).count()

    # Passenger class summary
    class_data = predictions.values(
        "passenger_class"
    ).annotate(
        total=Count("id")
    ).order_by("passenger_class")

    class_labels = [
        f"Class {item['passenger_class']}"
        for item in class_data
    ]

    class_counts = [
        item["total"]
        for item in class_data
    ]

    context = {
        "survivors": survivors,
        "non_survivors": non_survivors,
        "class_labels": class_labels,
        "class_counts": class_counts,
    }

    return render(
        request,
        "predictor/analytics.html",
        context
    )