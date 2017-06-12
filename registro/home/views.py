from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def pagina_principal_view(request):
	nombre = Estudiante.objects.all()
	return render(request,'index.html',locals())

def contacto_view(request):
	return render(request,'contacto.html',locals())

@login_required (login_url='/login/')
def agregar_registro_view(request):
	
	if request.method == "POST":
		form = agregar_registro_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			msg = "Guardado"
			#return redirect('/contactenos/')
			form = agregar_registro_form()
			return render(request,'agregar_registro.html',locals())
	else:	
		form = agregar_registro_form()
	return render(request,'agregar_registro.html',locals())

@login_required (login_url='/login/')
def editar_estudiante_view(request, id_est):
	obj = Estudiante.objects.get(pk = id_est)
	if request.method == "POST":
		form = agregar_registro_form(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			form.save()
			msg = "Guardado"
			#return redirect('/contactenos/')
			#form = agregar_registro_form()
			return render(request,'agregar_registro.html',locals())
	else:	
		form = agregar_registro_form(instance=obj)
	return render(request,'agregar_registro.html',locals())
	
def ver_estudiante_view(request,id_est):
	obj = Estudiante.objects.get(pk=id_est)
	return render(request,'ver_registro.html',locals())

@login_required (login_url='/login/')
def eliminar_estudiante_view(request,id_est):
	obj = Estudiante.objects.get(pk=id_est)
	obj.delete()
	return redirect('/')
	#return render(request,'index.html',locals())

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated(): #verificamos si el usuario ya esta authenticado o logueado  
		return redirect('/') #si esta logueado lo redirigimos a la pagina principal 
	else: #si no esta authenticado
		if request.method == "POST": 
			formulario = login_form(request.POST) #creamos un objeto de Loguin_form
			if formulario.is_valid(): # si la informacion enviada es correcta
				usu = formulario.cleaned_data['usuario'] #guarda informacion ingresada del formulario
				pas = formulario.cleaned_data['clave'] #guarda informacion ingresada del formulario
				usuario = authenticate(username = usu, password = pas)#asigna la autenticacion del usuario
				if usuario is not None and usuario.is_active:# si el usuario no es nulo y esta activo
					login(request, usuario) #se loguea al sistema con la informacion de usuario
					return redirect('/')# redirigimos a la pagina principal
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = login_form() #creamos un formulario nuevo en limpio
		return render(request, 'login.html',locals())

def logout_view(request):
	logout(request) #funcionde django importada anteriormente
	return redirect('/') # redirigimos a la pagina principal

