from django.db import models

class Advertisment(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length=200)
    cost = models.IntegerField()
    description = models.TextField()
    supplier = models.CharField(max_length = 200)
    expiration = models.DateField()

    def __str__(self):
        return "{} : {}".format(self.name, self.cost)