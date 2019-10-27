from django.forms import ModelForm
from .models import Employment

class EmploymentForm(ModelForm) :
    class Meta :
        model = Employment
        exclude = ()