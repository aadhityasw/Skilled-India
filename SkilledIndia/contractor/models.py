from django.db import models
from project.models import Project

class Contractor(models.Model) :
    name = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
