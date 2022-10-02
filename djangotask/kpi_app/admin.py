from django.contrib import admin
from kpi_app.models import KpiDevice,KpiInformation
# Register your models here.
admin.site.register(KpiInformation)
admin.site.register(KpiDevice)
