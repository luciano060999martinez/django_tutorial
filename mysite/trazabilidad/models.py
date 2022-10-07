from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Propietario(models.Model):
    nom_com=models.CharField(max_length=200)
    ruc = models.CharField(max_length=20)
    dir_local=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)
    departamento=models.CharField(max_length=100)
    ubicacion=models.CharField(max_length=100)
    act_no_act=models.BooleanField(default=True)


    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

class Animal(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=200)
    fecha_Nac = models.DateTimeField('Fecha nacimiento')
    sexo = models.CharField(max_length=200)
    listo_pro = models.BooleanField(default=False)
    peso_actual = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    Observaciones = models.CharField(max_length=500)
    #question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')

