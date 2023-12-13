from django import forms

from .models import Blog, Topic

class BlogForm(forms.ModelForm):
    topics = forms.ModelChoiceField(queryset=Topic.objects.all())
    class Meta:
        model = Blog
        fields = ['title', 'topics', 'text']
        labels = {'text': ''}
        widgets = {'title': forms.TextInput(attrs={'style': 'height: 30px;'}),
                   'topics': forms.Select(attrs={'style': 'height: 30px;'}),
                   'text': forms.Textarea(attrs={'cols': 80})
                   }
