from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=255)
# these are the schema declaration credientials which we have to specify in model to use in database

