from django.db import models

# Create your models here.
class Adduser(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    # # class Meta:
    # #     model = user
    # #     fields = ('id', 'username', 'email', 'password')
    def __str__(self):
        return self.username