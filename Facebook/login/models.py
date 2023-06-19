from django.db import models

# Create your models here.
class Index(models.Model):
    sF_Name = models.CharField(max_length=122)
    sL_Name = models.CharField(max_length=122)
    sM_Email = models.EmailField(max_length=122)
    # phone = models.CharField(max_length=12)
    sPass = models.CharField(max_length=145)
    choice = (
        '1', 'Male'
        '2', 'Female'
        '3', 'Not Know'
    )
    gender = models.CharField(max_length=10)
    date = models.DateField()