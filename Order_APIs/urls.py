
from django.contrib import admin
from django.urls import path ,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Order API Documentation",
      default_version='',
      description="API documentation for the Order application",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tanvirmahmud.cse66@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='api-doc-1'),
    path('doc/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='api-doc-2'),
]
