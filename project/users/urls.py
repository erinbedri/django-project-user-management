from django.urls import path

from project.users import views
from project.users.views import RegisterView

urlpatterns = [
    path('', views.home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
]
