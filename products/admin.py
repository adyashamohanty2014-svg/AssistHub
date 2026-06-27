from django.contrib import admin
from .models import Category, Device, Review, StoreLink

admin.site.register(Category)
admin.site.register(Device)
admin.site.register(Review)
admin.site.register(StoreLink)
