from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Destination


class DestinationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
        if self.user is None or not self.user.is_staff:
            self.fields['image'].widget = forms.HiddenInput()
            self.fields['featured'].widget = forms.CheckboxInput()

    class Meta:
        model = Destination
        fields = ['title', 'summary', 'description', 'location', 'image', 'featured']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3}),
        }


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
