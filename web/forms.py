from django import forms
from web.models import User, Employees

class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    post = forms.CharField(required=False)
    date_joined = forms.DateField(required=False)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password", "email", "date_joined")

class EmployeesForm(forms.ModelForm):
    user = UserForm()
    class Meta:
        model = Employees
        fields = "__all__"