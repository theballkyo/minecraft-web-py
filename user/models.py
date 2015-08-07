from django.db import models

class Account(models.Model):
    class Meta:
        db_table = "authme"
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    ip = models.CharField(max_length=40, default="127.0.0.1")
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    z = models.FloatField(default=0)
    world = models.CharField(max_length=40, default="world")
    lastlogin = models.BigIntegerField(default=1437558840388)
    isLogged = models.SmallIntegerField(default=0)

class Fe(models.Model):
    class Meta:
        db_table ="fe_accounts"
        unique_together = ('name','uuid')
    name = models.CharField(max_length=15, primary_key=True)
    uuid = models.CharField(max_length=36)
    money = models.FloatField()

class Inv(models.Model):
    class Meta:
        db_table = "multiinv_multiinv"
        #unique_together = ('id', 'inv_id')
    inv_id = models.BigIntegerField(primary_key=True)
    inv_group = models.CharField(max_length=50)
    inv_player = models.CharField(max_length=30)
    inv_uuid = models.CharField(max_length=36)
    inv_gamemode = models.CharField(max_length=20)
    inv_survival = models.TextField()