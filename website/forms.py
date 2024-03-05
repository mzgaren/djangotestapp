from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import Report

PARTNER_NAME_CHOICES = (
        ("user1", "Majdi"),
        ("user2", "Ali"),
        ("user3", "Jilani"),
    )
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

class AddReportForm(forms.ModelForm):
    user_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"User Name", "class":"form-control"}), label="")
    partner_name = forms.MultipleChoiceField(required=True, choices=PARTNER_NAME_CHOICES, widget=forms.CheckboxSelectMultiple)
    #partner_name = forms.MultipleChoiceField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Partner Name", "class":"form-control"}), label="")
    hours_worked1_partner_user = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Heure travailler", "class":"form-control"}), label="")
    hours_worked_main_user = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Heure travailler", "class":"form-control"}), label="")
    number_of_spots = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nbre de Spots", "class":"form-control"}), label="")
    number_of_boitier = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nbre Boitier", "class":"form-control"}), label="")
    raccordement = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"raccordement", "class":"form-control"}), label="")
    description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), label="")

    class Meta:
        model = Report
        exclude = ("user_name",)