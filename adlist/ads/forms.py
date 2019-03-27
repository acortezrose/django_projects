from django.forms import ModelForm
from ads.models import Ad

# Create the form class.
class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'
