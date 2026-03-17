from django.db import models

# Create your models here.
class Takeattedence(models.Model):
    technology=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return f"name:{self.name} date:{self.date} status:{self.status}"