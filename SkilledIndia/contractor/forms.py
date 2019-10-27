from django.forms import ModelForm
from .models import Contractor

class ContractorForm(ModelForm) :
    class Meta :
        model = Contractor
        exclude = ()