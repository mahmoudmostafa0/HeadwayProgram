from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,ListCreateAPIView

from kpi_app.models import KpiResult, KpiInformation
from kpi_app.serializers import KpiResultSerializer, KpiInformationSerializer


# Create your views here.
class KpiResultController(ListCreateAPIView):
    """
    API endpoint that allows kpi resuts to be viewed or edited.
    """
    queryset = KpiResult.objects.all()
    serializer_class = KpiResultSerializer


class KpiInformationController(ListCreateAPIView):
    """
    API endpoint that allows kpi resuts to be viewed or edited.
    """
    queryset = KpiInformation.objects.all()
    serializer_class = KpiInformationSerializer
