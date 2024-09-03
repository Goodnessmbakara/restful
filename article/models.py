from django.db import models

# Create your models here.

class Article(models.Model):
    owner = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null =True, blank=True)
    body = models.TextField(null = True, blank=True)