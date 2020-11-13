from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)


class ListForSpecialty(models.Model):
    name = models.CharField(max_length=100)
    related_specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)





