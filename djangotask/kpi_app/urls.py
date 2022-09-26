from django.urls import path

from kpi_app.views import KpiResultController, KpiInformationController

urlpatterns = [
    path('kpi_results', KpiResultController.as_view()),
    path('kpi_info', KpiInformationController.as_view())
]
