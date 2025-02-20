from django.db import models

class Coachings(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    brief=models.TextField()
    contact=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Query(models.Model):
    your_name=models.CharField(max_length=50)
    your_email=models.CharField(max_length=35)
    subject=models.CharField(max_length=100)
    message=models.TextField()
