from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly

# Create your views here.

class SpecialzationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view ):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class AvilableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # item par page
    page_size_query_param = page_size
    max_page_size = 100



class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination
    search_fields = ['user_first_name', 'user_email', 'designation_name', 'specialization_name']
    

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer