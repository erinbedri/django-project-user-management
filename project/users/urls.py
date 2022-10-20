from django.urls import path

from project.users import views

urlpatterns = [
    path('', views.home, name='users-home'),
]
