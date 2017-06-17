from django import forms
from .models import UserDetails
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=75, widget=forms.TextInput(attrs={'class': 'form-control','required': 'required' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'required': 'required'}))

    def clean_email(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        # current_user = self.instance.email
        if not User.objects.filter(email=email):
            raise forms.ValidationError("This email does not exist !")
        return email

class SignUpForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','required':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','required':'required'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'required':'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required':'required'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required':'required'}))

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        # current_user = self.instance.email
        if not confirm_password == password:
        # if not User.objects.filter(email=email):
            raise forms.ValidationError("Password not match with Confirm Password !")
        return cleaned_data

    def clean_email(self):
        cleaned_data = super(SignUpForm, self).clean()
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError("This email already exist !")
        return email

# class UserDetailsForm(forms.ModelForm):
#     class Meta:
#         model = UserDetails
#         fields = ('user_description', 'image', 'state', 'city', 'mobile_no', 'address')
#         # widgets = {
#         #     'image': FileInput(),
#         # }
#
#     def __init__(self, *args, **kwargs):
#         super(UserDetails, self).__init__(*args, **kwargs)
#         self.fields['image'].widget.attrs.update({'class': 'form-control'})
#         self.fields['city'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
#         self.fields['state'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
#         self.fields['mobile_no'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
#         self.fields['address'].widget.attrs.update({'class': 'form-control', 'cols': '100', 'rows': '5', 'required': 'required'})
#         self.fields['user_description'].widget.attrs.update({'class': 'form-control', 'cols': '100', 'rows': '5', 'required': 'required'})

    # class Meta:
    #     model = UserDetails
    #     fields = ('image', 'state', 'city', 'mobile_no', 'address', 'first_name', 'last_name', 'email', 'password', 'confirm_password')
    #     widgets = {
    #         'image': FileInput(),
    #     }
    #
    # def __init__(self, *args, **kwargs):
    # super(ProfileForm, self).__init__(*args, **kwargs)
    # self.fields['image'].widget.attrs.update({'class': 'py-form-control'})
    # self.fields['state'].widget.attrs.update({'class': 'py-form-control', 'required': 'required'})
    # self.fields['mobile_no'].widget.attrs.update({'class': 'py-form-control', 'required': 'required'})
    # self.fields['address'].widget.attrs.update({'class': 'py-form-control', 'cols': '100', 'rows': '5', 'required': 'required'})
