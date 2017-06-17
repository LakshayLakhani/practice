from django import forms
from django.forms import ModelForm,NumberInput,TextInput,DateTimeInput, DateInput, FileInput, ModelChoiceField

from accounts.models import UserDetails
from .models import Posts
# from django.contrib.auth.models import User

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('user_description', 'image', 'state', 'city', 'mobile_no', 'address')
        widgets = {
            'image': FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserDetailsForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['mobile_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'cols': '100', 'rows': '5'})
        self.fields['user_description'].widget.attrs.update({'class': 'form-control', 'cols': '100', 'rows': '5'})


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('status','image')
        widgets = {
            'image': FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(PostsForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control', 'cols': '100', 'rows': '5'})
        self.fields['image'].widget.attrs.update()
