"""api_automation_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.urls import re_path
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, \
    SpectacularJSONAPIView

from api_test import urls
from api_test.api.ApiDoc import MockRequest
#
# schema_view = get_schema_view(title='测试平台 API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
#                               , permission_classes=())
urlpatterns = [
    re_path('swagger/json/', SpectacularJSONAPIView.as_view(), name='schema'),
    # Optional UI:
    re_path('swagger/schema/', SpectacularAPIView.as_view(), name='schema'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    re_path('admin/', admin.site.urls),
    re_path(r'^$', TemplateView.as_view(template_name="index.html")),
    re_path(r'^api/', include(urls)),
    path('mock/<path:apiAdr>', MockRequest.as_view()),
]
