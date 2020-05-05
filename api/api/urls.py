from django.conf.urls import include, url
from django.contrib import admin
from core.views import ClienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]
