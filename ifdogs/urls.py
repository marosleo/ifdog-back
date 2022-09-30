from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
# from core.views import RegistrationAPIView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from core import views
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import CachorroViewSet, ComedouroViewSet, TagViewSet, PublicacoesViewSet, RegistrationViewSet, ComentariosViewSet, MyTokenObtainPairView

router = DefaultRouter()
router.register(r'cachorros', CachorroViewSet)
router.register(r'comedouro', ComedouroViewSet)
router.register(r'tags', TagViewSet)
router.register(r'publis', PublicacoesViewSet)
router.register(r'auth', RegistrationViewSet)
router.register(r'coments', ComentariosViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('register/', RegistrationAPIView.as_view(), name='register'),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

