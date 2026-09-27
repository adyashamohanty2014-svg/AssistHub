from django.urls import path
from . import views

urlpatterns = [
    path("", views.ask_ai, name="ask_ai"),
    path("api/", views.ask_ai_api, name="ask_ai_api"),
]