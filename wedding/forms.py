from django import forms

class ConfirmAssistance(forms.Form):
    name = forms.CharField(label='Nombre y apellidos', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    attendance = forms.CharField(label='¿Vienes?', max_length=50)
    how_many = forms.IntegerField(label='¿Cuántos seréis?')

class MakeSuggestion(forms.Form):
    suggestion = forms.CharField(label='Sugerencia', max_length=240)