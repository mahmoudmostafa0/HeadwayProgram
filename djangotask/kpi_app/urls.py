from django.urls import path

from kpi_app import views
from kpi_app.views import KpiInformationController, KpiDeviceController

urlpatterns = [
    path('kpi_info', KpiInformationController.as_view()),
    path('kpi_link_device', KpiDeviceController.as_view()),
    path('send_message', views.send_message)
]
