from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    Name        = models.CharField(max_length=40,null=False,blank=False)
    Edition     = models.DecimalField(max_digits=6,blank=True,decimal_places=2)
    Author      = models.CharField(max_length=40,default='None')
    Description = models.TextField(null=True,default='TYPE YOUR DESCRIPTION')
    Quantity    = models.IntegerField(default=1)
    Issue_To    = models.CharField(default='None',max_length=40)
    Status      = models.BooleanField(default=True)
    def __str__(self):
        return self.Name


class Issue(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    book=models.OneToOneField(Book,on_delete=models.CASCADE)
    issued=models.DateField(auto_now_add=True)
    fine=models.FloatField(default=0.0)
    returndate=models.CharField(max_length=40,default='')
    def __str__(self):
        return str(self.user.username)+str("->")+str(self.book.Name)