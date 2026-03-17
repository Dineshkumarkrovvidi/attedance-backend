from django.db import models

# Create your models here.
class Addattedance(models.Model):
    technology=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return self.name