from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='devices/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
# Create your models here.
