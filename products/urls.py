from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy


urlpatterns = [
 path('',views.home, name='home'),
 path('login/', views.user_login, name='login'),
 path('register/', views.register, name='register'),
 path('devices/', views.device_list, name='device_list'),
 path('device/<int:id>/', views.device_detail, name='device_detail'),
 path('category/<int:category_id>/',views.category_devices,name='category_devices'),
 path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
 path('profile/', views.profile, name='profile'),
 path('profile/edit/', views.edit_profile, name="edit_profile"),
 path("password-change/", auth_views.PasswordChangeView.as_view(template_name="products/password_change.html",success_url=reverse_lazy("password_change_done"),),name="password_change",),
 path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="products/password_change_done.html"), name="password_change_done"),
 path("my-reviews/",views.my_reviews,name="my_reviews",),
 path("review/<int:review_id>/edit/",views.edit_review,name="edit_review"),
 path('wishlist/<int:id>/',views.toggle_wishlist,name='toggle_wishlist'),
 path('my-wishlist/',views.my_wishlist,name='my_wishlist'),
 path("about/", views.about, name="about"),
 path("contact/", views.contact, name="contact"),
 path('cart/<int:device_id>/',views.toggle_cart,name='toggle_cart'),
 path('my-cart/',views.my_cart,name='my_cart'),
 path('compare/', views.compare_view, name='compare'),
 path(
    'review/<int:review_id>/delete/',
    views.delete_review,
    name='delete_review'
),
]