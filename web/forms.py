from django import forms
from web.models import User, Employees

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class EmployeesForm(forms.ModelForm):
    user = UserForm()
    class Meta:
        model = Employees
        fields = "__all__"