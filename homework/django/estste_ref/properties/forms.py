from django import forms
from properties.models import DealRequest, Property


class DealRequestForm(forms.ModelForm):
    class Meta:
        model = DealRequest
        exclude = ('seeker', 'property', 'status')
        fields = ('message', )

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ('owner', )
