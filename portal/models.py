from django.db import models

class account(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    ip = models.CharField(max_length=40)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    world = models.CharField(max_length=40)
    lastlogin = models.BigIntegerField()
    isLogged = models.SmallIntegerField()

class fe(models.Model):
    name = models.CharField(max_length=15)
    uuid = models.CharField(max_length=36)
    money = models.FloatField()
