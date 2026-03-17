from django.shortcuts import render
from rest_framework import viewsets
from .models import Addattedance
from .serializer import AttendanceSerializer
# Create your views here.
class AddAttedenceView(viewsets.ModelViewSet):
    queryset = Addattedance.objects.all()
    serializer_class=AttendanceSerializer