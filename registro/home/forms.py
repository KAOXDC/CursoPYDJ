from django import forms
from .models import Estudiante
from django.contrib.auth.models import User


class agregar_registro_form(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = '__all__'
		#exclude = ['user','correo']
class login_form(forms.Form):
	usuario	= forms.CharField(widget = forms.TextInput())
	clave 	= forms.CharField(widget = forms.PasswordInput(render_value = False))
'''
class registro_users(fOrms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
'''