from django.db import models
from users.models import*

class Advertisment(models.Model):
    user = models.ManyToManyField(CustomUser)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

__CATEGORY = ['سگ', 'گربه', 'ماهی', 'پرنده', 'جونده', 'خزنده']
CATEGORY_CHOICES = [(item, item) for item in __CATEGORY]

class Product(models.Model):
    name = models.CharField(max_length = 200)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=200)
    cost = models.IntegerField()
    description = models.TextField()
    # supplier = models.CharField(max_length = 200)
    # expiration = models.DateField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "{} : {}".format(self.name, self.cost)

class Vet(models.Model):
    username = models.CharField(max_length = 200)
    description = models.TextField()
    axprofile = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username