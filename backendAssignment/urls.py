from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from userapp.views import UserViewSet

router = DefaultRouter()
router.register("users",UserViewSet,basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
