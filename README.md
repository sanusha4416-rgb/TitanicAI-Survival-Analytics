
# TitanicAI - Survival Analytics Platform

A Machine Learning-powered web application built with Django to predict Titanic passenger survival based on passenger details.

## Project Overview

TitanicAI allows users to enter passenger information and receive a survival prediction with an estimated survival probability. The platform also provides user authentication, a personal dashboard, prediction history, and analytics.

## Features

- Passenger survival prediction using a trained Random Forest model
- Survival probability display
- User registration and login
- Personal dashboard with prediction statistics
- Prediction history for logged-in users
- Analytics charts for prediction results and passenger classes
- Form validation
- Responsive user interface

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Django
- **Machine Learning:** Scikit-learn, Random Forest
- **Data Processing:** Pandas, NumPy
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Data Visualization:** Chart.js
- **Version Control:** Git and GitHub

## Machine Learning Model

The application uses a trained Random Forest classification model.

Input features include:
- Passenger class (Pclass)
- Sex
- Age
- Siblings and spouses aboard (SibSp)
- Parents and children aboard (Parch)
- Fare
- Port of embarkation (Embarked)

The model and its expected input columns are stored as serialized files in the `predictor` application.

## Project Structure

```text
titanic_web/
├── manage.py
├── requirements.txt
├── titanic_web/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── predictor/
    ├── migrations/
    ├── static/
    │   └── predictor/css/
    ├── templates/
    │   └── predictor/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── titanic_model.pkl
    └── titanic_columns.pkl
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sanusha4416-rgb/TitanicAI-Survival-Analytics.git
cd TitanicAI-Survival-Analytics
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the local URL in your browser:

http://127.0.0.1:8000/

## Usage

1. Open the application in your browser.
2. Register an account or log in.
3. Enter passenger details on the prediction page.
4. View the predicted survival outcome and probability.
5. Explore your dashboard, prediction history, and analytics.

## Important Notes

- Predictions are model estimates, not guarantees of actual survival.
- Model performance depends on the training data and feature preprocessing.
- The application is currently intended as a learning and portfolio project.
- Before production deployment, configure secure Django settings, environment variables, HTTPS, and an appropriate production database.

## Future Improvements

- Deploy the application online
- Add model evaluation reports and visualizations
- Improve prediction explanations
- Add automated tests
- Enhance mobile responsiveness

## Author

**Sanusha M**

GitHub: [sanusha4416-rgb](https://github.com/sanusha4416-rgb)

Project Repository: [TitanicAI-Survival-Analytics](https://github.com/sanusha4416-rgb/TitanicAI-Survival-Analytics)
