from django import forms
from .models import CarService
from .models import CarEstimate

class NewsSearchForm(forms.Form):
    keyword = forms.CharField(label='Enter a keyword', max_length=100)


# CarService Form
# Assuming you have a model named CarService
# class CarService(models.Model):
class CarServiceForm(forms.ModelForm):
    class Meta:
        model = CarService
        fields = [
            'car_model',
            'service_type',
            'repair_cost',
            'service_notes',
        ]
class CarEstimateForm(forms.ModelForm):
    class Meta:
        model = CarEstimate
        fields = '__all__'