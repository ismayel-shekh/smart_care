from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amadar rowter
router.register('', views.ContactusViewset) # rowter ar antena
urlpatterns = [
    path('', include(router.urls)),
]
