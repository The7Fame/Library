from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)
	city = forms.CharField(max_length=30, required=False)
	date_of_birth = forms.DateField(required=False)

	class Meta:
		model = User
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
	username = forms.CharField(max_length=30, required=False)
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)

	class Meta:
		model = Profile
		fields = ['city', 'date_of_birth']