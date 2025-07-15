from django import forms
from vacancy.models import Vacancy


class VacancyAddForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        # exclude = ('seeker', 'property', 'status')
        # fields = ('name',)
        exclude = ('name', 'added_at')

class VacancyRemoveForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        # exclude = ('seeker', 'property', 'status')
        # fields = ('remove-number',)
        fields = ('id',)

class VacancyShowForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        # exclude = ('seeker', 'property', 'status')
        # fields = ('name', 'added_at')
        exclude = ('name', 'added_at')
