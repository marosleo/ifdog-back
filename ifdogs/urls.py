from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import CachorroViewSet, ComedouroViewSet, TagViewSet, PublicacoesViewSet, RegistrationViewSet, ComentariosViewSet, MyTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from media.router import router as media_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

path("api/media/", include(media_router.urls)),

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
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/",SpectacularSwaggerView.as_view(url_name="schema"),
    name="swagger-ui",
    ),
    path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"),
    name="redoc",
    ),
    
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
