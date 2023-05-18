from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

# Create your models here.
class Act(models.Model):
    num = models.IntegerField(verbose_name="Acta N°")
    pub_date = models.DateTimeField()
    process_text = models.CharField(max_length=200)
    type_meet = models.CharField(max_length=20)
    hour = models.DateTimeField(max_length=200) #
    next_meet = models.DateTimeField(max_length=200)
    place = models.CharField(max_length=200)
    
    def __str__(self):
        return self.pk
    
class Job(models.Model):
    name_job = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.pk
  
class User(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    job_position = models.ForeignKey(Job,on_delete =models.CASCADE)
    attended =  models.CharField(max_length=200)#revisar
    approve = models.CharField(max_length=200)
    asset = models.BooleanField()
    num_id = models.IntegerField()
    process = models.CharField(max_length=40)


    def __str__(self):
        return self.pk
           
    
class Confirmation(models.Model):
    user_id = models.ForeignKey(User,on_delete =models.CASCADE)
    act_id = models.ForeignKey(Act,on_delete =models.CASCADE)

    def __str__(self):
        return self.pk
    
class Commitment(models.Model):
    date = models.DateTimeField("Data publish") 
    observations = models.CharField(max_length=200)
    commitment =  models.CharField(max_length=200)
    control =  models.CharField(max_length=200)

    def __str__(self):
        return self.pk

class Responsiblecommitment(models.Model):
    user_id = models.ForeignKey(User,on_delete =models.CASCADE)
    commitment_id = models.ForeignKey(Commitment,on_delete =models.CASCADE)
    
    def __str__(self):
        return self.pk
    
class Development(models.Model):
    act_id = models.ForeignKey(Act,on_delete =models.CASCADE)
    num = models.IntegerField()
    tittle =  models.CharField(max_length=200)
    agreements =  models.CharField(max_length=200)
    description =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.pk
    
class Responsibledevelopment(models.Model):
    user_id = models.ForeignKey(User,on_delete =models.CASCADE)
    commitment_id = models.ForeignKey(Development,on_delete =models.CASCADE)
    user_name=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.pk
    
