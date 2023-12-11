from django.db import models
from django.contrib.auth.models import User

class AnswerPQRS(models.Model):
    answer = models.TextField(verbose_name="Respuesta")
    response_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Respuesta")
    
    def _str_(self):
        return self.pqrs
    
    class Meta:
        verbose_name = 'Respuesta' 
        verbose_name_plural = 'Respuestas'
        db_table = 'respuestas' 
        ordering = ['id']

class PQRS(models.Model):
    case = models.CharField(max_length=100, verbose_name="Asunto")
    description = models.TextField(verbose_name="Descripción")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    answer = models.ForeignKey(AnswerPQRS, on_delete=models.CASCADE, verbose_name="Respuesta" )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    def _str_(self):
        return self.asunto
    
    class Meta:
        verbose_name = 'Comentario' 
        verbose_name_plural = 'Comentarios'
        db_table = 'comentarios' 
        ordering = ['id']
    
