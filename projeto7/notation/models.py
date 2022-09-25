from django.db import models

#tabela onde fica o registro de atividades
class tb_works(models.Model):
	title=models.CharField(max_length=80)
	subtitle=models.CharField(max_length=80)
	work=models.TextField()
	timestamp=models.DateTimeField(auto_now=True)