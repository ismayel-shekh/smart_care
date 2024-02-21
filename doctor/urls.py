from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()
router.register('list', views.DoctorViewset)
router.register('designation', views.DesignationViewset)
router.register('spacialization', views.SpecialzationViewset)
router.register('available_time', views.AvilableTimeViewset)
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls))
]
