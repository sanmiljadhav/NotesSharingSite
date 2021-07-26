from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,null=True)
    branch = models.CharField(max_length=20)
    role = models.CharField(max_length=15)
    def __str__(self):
        return self.user.username
    

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField()
    filetype = models.CharField(max_length=30)
    desc = models.TextField()
    status = models.CharField(max_length=15)

