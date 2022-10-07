import datetime
from email.policy import default

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):

    question_text = models.CharField(max_length=200) #1
    pub_date = models.DateTimeField('date published') #1
    #test = models.BooleanField(default=True)
    def __str__(self): #2
        return self.question_text  #2
    def was_published_recently(self): #2 #prueba
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #1
    choice_text = models.CharField(max_length=200) #1
    votes = models.IntegerField(default=0) #1
    def __str__(self): #2
        return self.choice_text #2