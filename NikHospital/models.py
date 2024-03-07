from django.db import models
import datetime
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=150)


    def __str__(self):
        return self.email
class Registration(models.Model):
    name = models.CharField(max_length=50)
    phon = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=150)
    # confirm_password = models.CharField(max_length=150)

    # def set_password(self,raw_password):
    #     self.password = make_password(raw_password)
    #
    # def check_password(self,raw_password):
    #     return check_password(raw_password,self.password)

    def __str__(self):
        return self.name
class Booking(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    # date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField(default=datetime.time(0, 0))
    # time = models.TimeField()
    def __str__(self):
        return self.name

