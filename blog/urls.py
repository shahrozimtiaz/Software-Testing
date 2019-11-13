from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('login/', views.loginPage, name='loginPage'),
    # path('makePost/', views.makePost, name='makePost'),
    path('', views.posts, name='posts'),
    path('signout/', views.signout, name='signout'),
]