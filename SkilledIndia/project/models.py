from django.db import models


class Project(models.Model) :
    name = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    skilled_workforce_count = models.IntegerField()
    unskilled_workforce_count = models.IntegerField()
    skilled_workforce_sal = models.DecimalField(max_digits=10, decimal_places=2)
    unskilled_workforce_sal = models.DecimalField(max_digits=10, decimal_places=2)
    skilled_workforce_age = models.IntegerField()
    unskilled_workforce_age = models.IntegerField()
    location = models.CharField(max_length=200)

    sector_choices = [('U', 'Urban'), ('R', 'Rural')]
    sector = models.CharField(max_length=1, choices=sector_choices, default='U')

    def __str__(self):
        return self.name
    