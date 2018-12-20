from django import forms

class ConfirmAssistance(forms.Form):
    name = forms.CharField(label='Nombre y apellidos', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    attendance = forms.BooleanField(label='¿Vienes?')
    how_many = forms.IntegerField(label='¿Cuántos seréis?')