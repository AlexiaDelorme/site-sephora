from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=150)


class SubSpecialty(models.Model):
    name = models.CharField(max_length=100)
    related_specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)


class ListForSubSpecialty(models.Model):
    name = models.CharField(max_length=100)
    related_sub_specialty = models.ForeignKey(SubSpecialty, on_delete=models.CASCADE)
