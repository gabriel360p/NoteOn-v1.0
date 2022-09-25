from django.shortcuts import render
from .models import tb_works #tabela de atividades
from django.http import HttpResponse

#importei o redirect que serve para fazer redirecionamentos
from django.shortcuts import redirect
#e importei as urls para views, desse jeito eu tenho acesso as urls e consigo fazer o redirecionamento das páginas usando o redirect!!
from . import urls #importando as rotas/urls da aplicação para conseguir fazer redirecionamentos de páginas

# https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#redirect


def viewtarefas(request): #página onde mostra as tarefas
	works=tb_works.objects.all()
	return render(request,'tarefas.html',{'work':works})

def viewnova (request): #formulário para criar a nova tarefa
	return render(request,'newtarefa.html')

def vieweditar(request,id): #formulário para criar a nova tarefa
	works=tb_works.objects.get(pk=id)
	return render(request,'editartarefa.html',{'work':works})

#formulario de nova tarefa
def addtarefa(request):
	if request.method=="POST":
		titulo=request.POST.get('titulo')
		subtitulo=request.POST.get('subtitulo')
		texto=request.POST.get('texto')
		#mandano para o banco de dados
		work=tb_works(title=titulo,subtitle=subtitulo,work=texto)
		#salvando no banco de dados
		work.save()
		return redirect ('notation:tarefas') #usando redirect para acessar as urls e redirecionar as páginas

#funcionouuuuuuuuuu
def editartarefa(request,id):
	if request.method=="POST":
		work=tb_works.objects.get(pk=id)
		work.title=request.POST.get('titulo')
		work.subtitle=request.POST.get('subtitulo')
		work.work=request.POST.get('texto')
		work.save()
		return redirect ('notation:tarefas') #usando redirect para acessar as urls e redirecionar as páginas

#apagando tarefa
def deletetarefa(request,id):
	work=tb_works.objects.get(pk=id)
	work.delete()
	return redirect ('notation:tarefas') #usando redirect para acessar as urls e redirecionar as páginas
