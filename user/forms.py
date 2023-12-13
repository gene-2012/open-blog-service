from django import forms
from django.contrib.auth import get_user_model


class PageForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'page', 'avatar']
        labels = {'username': 'username:', 'page': 'page:', 'avatar': 'avatar:'}
        widgets = {'username': forms.TextInput(),'page': forms.Textarea(),'avatar':forms.ImageField()}