"""
URL configuration for dobriki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


class InconsistentNestedApiSchemaGenerator(OpenAPISchemaGenerator):
    """
    if we got no common prefix, we need this stuff to get okaish tags in schema
    """

    version_path = re.compile(r"/?api/(?:(v\d+)/)?([^/]+)")

    def get_schema(self, *args, **kwargs):  # noqa: ANN201
        schema = super().get_schema(*args, **kwargs)
        for item_path, item in schema.paths.items():
            match = self.version_path.match(item_path)
            if not match:
                continue
            ver, tag = match.groups()
            for _, op in item.operations:
                # ver may not be found
                op.tags = [f"{tag} {ver or ''}".rstrip()]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Dobriki API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[AllowAny],
    generator_class=InconsistentNestedApiSchemaGenerator,
)

urlpatterns = [
    path('api/auth/', include('accounts.urls')),
    path('api/feed/', include('feed.urls')),
    path('api/', include('charity.urls')),
    path('api/competitions/', include('competitions.urls')),
    path("swagger", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('admin/', admin.site.urls),
    path('api/activity/', include('activity.urls')),
    path('api/', include('achievement.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
