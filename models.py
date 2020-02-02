from django.db import models
from django.db.models import Model
# Create your models here.
class campaign(models.Model):
    camp_name= models.CharField(max_length=100)
    venue= models.CharField(max_length=100)
    time= models.DateTimeField()
    img=models.ImageField(upload_to='photo')
    desc=models.TextField()
    
