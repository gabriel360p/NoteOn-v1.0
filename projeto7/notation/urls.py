from django.urls import path
from . import views

app_name="notation"

urlpatterns=[
	#pags:
	path('home/',views.viewtarefas,name="tarefas"),
	path('nova/',views.viewnova,name="nova"),
	path('editar/<int:id>',views.vieweditar,name="editar"), 



	path('inserir/',views.addtarefa,name="add"),
	path('delete/<int:id>',views.deletetarefa,name="delete"),
	path('edit/<int:id>',views.editartarefa,name="edit"),
]