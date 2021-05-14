from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email =  models.EmailField()
    message = models.TextField()


class Files(models.Model):
    adminupload=models.FileField(upload_to='media')
    tittle=models.CharField(max_length=50)

    def __str__(self):
        return self.tittle