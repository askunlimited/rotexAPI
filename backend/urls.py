from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from product import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/products/", include("product.urls")),
    # path('api/', include(router.urls)),
    # path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    # path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name="schema")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
