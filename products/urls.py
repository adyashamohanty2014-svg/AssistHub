from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
 path('',views.home, name='home'),
 path('login/', views.user_login, name='login'),
 path('register/', views.register, name='register'),
 path('devices/', views.device_list, name='device_list'),
 path('device/<int:id>/', views.device_detail, name='device_detail'),
 path('category/<int:category_id>/',views.category_devices,name='category_devices'),
 path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]