from django.db import models


# Create your models here.

class KpiInformation(models.Model):
    """
    model to save kpi expressions
    """
    name = models.CharField(max_length=30)
    expression = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"name : {self.name}, primary key: {self.id}"


class KpiMessage(models.Model):
    asset_id = models.IntegerField(primary_key=True)
    attribute_id = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    value = models.CharField(max_length=50)

    def __str__(self):
        return f"value : {self.value}, primate key: {self.asset_id}"


class KpiResult(models.Model):
    message_asset_id = models.ForeignKey(KpiMessage, on_delete=models.CASCADE)
    message_kpi_expression = models.ForeignKey(KpiInformation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    result = models.CharField(max_length=50)
