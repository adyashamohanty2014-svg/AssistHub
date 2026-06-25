from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )

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
    buy_link = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
    def average_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            return round(
                sum(r.rating for r in reviews) / reviews.count(),1)
        return 0

#Review Section
class Review(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.device.name}"