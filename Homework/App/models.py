from django.db import models

class User(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=35, default=None)

    def __str__(self):
        return self.login
