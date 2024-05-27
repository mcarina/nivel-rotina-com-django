from django.urls import path
from rest_framework.routers import SimpleRouter
from .views_v1 import *

router = SimpleRouter()
urlpatterns = [
    path('usuarios/', UsuariosListView.as_view(), name = "usuarios"),
]