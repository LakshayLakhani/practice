from django import forms

class MsgForm(forms.Form):
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '', 'rows': '', 'required': 'required'}))
