from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import User
class Instituto(models.Model):
	nombre 		= models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.nombre 

# Create your models here.
class Estudiante(models.Model):
	documento	= models.IntegerField()
	nombre 		= models.CharField(max_length=200)
	direccion 	= models.CharField(max_length=200)
	edad 		= models.IntegerField()
	correo 		= models.EmailField(blank=True,null=True)
	foto 		= models.ImageField(upload_to='fotos',blank=True,null=True)
	#user 		= models.OneToOneField(User)
	instituto 	= models.ForeignKey(Instituto)
	#instituto 	= models.ManyToManyField(Instituto)

	def __unicode__(self):
		return self.nombre + " " +  self.direccion
	
