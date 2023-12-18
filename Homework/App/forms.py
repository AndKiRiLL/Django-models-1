from django import forms

class Form(forms.Form):
    email = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'email', 'placeholder': 'ivanov_ivan@mail.ru'}))

    password = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'password', 'placeholder': '***********'}))

    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__title__input__top form__block__input', 'name': 'name', 'placeholder': 'Ivan123'}))

