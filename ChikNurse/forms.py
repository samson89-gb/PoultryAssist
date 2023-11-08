from django import forms

class SymptomInputForm(forms.Form):
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        label='Symptoms'
    )