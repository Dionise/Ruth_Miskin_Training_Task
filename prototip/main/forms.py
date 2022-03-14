from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015')
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	birthdate = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years = DOY))
    
	class Meta:
		model = User
		fields = ("username","first_name","last_name", "email", "password1", "password2", "birthdate")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user
