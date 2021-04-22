from django import forms
from .models import BookMark

class BookMarkForm(forms.ModelForm):

    class Meta:
        model = BookMark
        fields = ('name', 'description', 'url', 'tags')