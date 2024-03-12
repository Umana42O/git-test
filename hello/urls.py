from django.urls import path
from . import views

urlpatterns = [
    path("<str:saludo>", views.hello),
]