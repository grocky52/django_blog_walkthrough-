from django.urls import path
from . import views 
from users import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),

]