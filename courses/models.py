from django.db import models

class Course(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=255)
    text2=models.TextField()
    text3=models.CharField(max_length=255)
