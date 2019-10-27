from django.db import models
from project.models import Project

class Employment(models.Model) :
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    project_title = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    email_address = models.CharField(max_length=200, blank=True)
    option_list = (('S', 'Skilled'), ('U', 'Unskilled'))
    job_type = models.CharField(max_length=1, choices=option_list, default='U')


    def __str__(self):
        return self.name

