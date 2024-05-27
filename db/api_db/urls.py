from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views_v1 import UsuariosViewSet

router = SimpleRouter()
router.register('usuarios', UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
