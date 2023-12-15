from django import forms
from django.contrib.auth import get_user_model


class PageForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'page', ]
        labels = {'username': 'username:', 'page': 'page:', }
        widgets = {'username': forms.TextInput(),'page': forms.Textarea()}