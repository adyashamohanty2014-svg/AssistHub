from django.contrib import admin
from .models import Category, Device, Review, StoreLink, Contact

admin.site.register(Category)
admin.site.register(Device)
admin.site.register(Review)
admin.site.register(StoreLink)
admin.site.register(Contact)
