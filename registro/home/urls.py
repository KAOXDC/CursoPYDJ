from django.conf.urls import url
from .views import * 
urlpatterns=[
	url(r'^$',pagina_principal_view,name='principal'),
	url(r'^contactenos/$',contacto_view,name='contacto'),
	url(r'^agregar_registro/$',agregar_registro_view,name='agregar_registro'),
	url(r'^editar_estudiate/(?P<id_est>.*)/$', editar_estudiante_view, name='editar_estudiante'),
	url(r'^ver_estudiate/(?P<id_est>.*)/$', ver_estudiante_view, name='ver_estudiante'),
	url(r'^eliminar_estudiate/(?P<id_est>.*)/$', eliminar_estudiante_view, name='eliminar_estudiante'),
	
	url(r'^login/$', login_view, name = 'vista_login'),
	url(r'^logout/$', logout_view, name = 'vista_logout'),

		
]
