from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Prediction(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="predictions"
    )

    passenger_class = models.IntegerField()
    sex = models.CharField(max_length=10)
    age = models.FloatField()
    siblings_spouses = models.IntegerField()
    parents_children = models.IntegerField()
    fare = models.FloatField()
    embarked = models.CharField(max_length=1)

    prediction_result = models.IntegerField()
    survival_probability = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Prediction {self.id}"
