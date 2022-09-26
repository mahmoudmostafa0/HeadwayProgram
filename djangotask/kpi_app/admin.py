from django.contrib import admin
from kpi_app.models import KpiInformation,KpiMessage,KpiResult
# Register your models here.
admin.site.register(KpiInformation)
admin.site.register(KpiMessage)
admin.site.register(KpiResult)