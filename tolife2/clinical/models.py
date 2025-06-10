from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Patient(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_of_study = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ClinicalParameter(models.Model):
    name_parameter = models.CharField(max_length=255)
    parameter = models.CharField(max_length=100)
    units = models.CharField(max_length=50, default="unknown")

    def __str__(self):
        return f"{self.name_parameter} ({self.parameter})"


class ClinicalMeasurement(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="measurements",
    )
    parameter = models.ForeignKey(
        ClinicalParameter,
        on_delete=models.CASCADE,
        related_name="measurements",
    )
    timestamp = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.parameter.parameter} ({self.timestamp}): {self.value}"
