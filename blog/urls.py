from django.urls import path
from . import views
from users import views as user_views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name = 'about')

]