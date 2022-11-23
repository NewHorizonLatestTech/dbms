from django.db import models

# Create your models here.
class dbsqlite(models.Model):
    name=models.CharField(max_length=50,default="")
    age=models.CharField(max_length=50,default="")
    password=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    father_name=models.CharField(max_length=50,default="")
    our_image=models.ImageField(upload_to="image",default="")
    def __str__(self):
        return self.name
 
    
