from django.urls import path
from . import views 
from .views import  postlistview, postdetailview, postcreateview, postupdateview, postdeleteview
from users import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'blog'
urlpatterns = [
    path('', postlistview.as_view(), name = 'home'),
    path('post/<int:pk>/', postdetailview.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update/', postupdateview.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', postdeleteview.as_view(), name = 'post-delete'),
    path('post/new/', postcreateview.as_view(), name = 'post-create'),
    path('about/', views.about, name = 'about'),

]