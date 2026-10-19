from django.contrib import admin
from .models import Prediction

# Register your models here.

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "passenger_class",
        "prediction_result",
        "survival_probability",
        "created_at",
    )

    list_filter = ("prediction_result", "created_at")
    search_fields = ("user__username",)
