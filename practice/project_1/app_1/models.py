from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length=254)
    last_name  = models.CharField(max_length=254)
    email      = models.EmailField(unique=True)




