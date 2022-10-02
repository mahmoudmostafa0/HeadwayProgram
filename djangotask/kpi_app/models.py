from django.db import models


# Create your models here.

class KpiInformation(models.Model):
    """
    model to save kpi expressions
    """
    name = models.CharField(max_length=30)
    expression = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

    # link kpi equation with one attribute id (leave for now)
    # link kpi equation with many asset ids
    def __str__(self):
        return f"{self.name}"


class KpiDevice(models.Model):
    asset_id = models.CharField(max_length=50)
    kpi_id = models.ForeignKey(KpiInformation, related_name='assets', on_delete=models.CASCADE)

    # def __str__(self):
    #  return self.__dict__

    class Meta:
        unique_together = ['asset_id', 'kpi_id']


class KpiMessageEquationResult(models.Model):
    kpi_equation = models.ForeignKey(KpiInformation, on_delete=models.CASCADE)
    kpi_message = models.ForeignKey("KpiMessage", on_delete=models.CASCADE)
    value = models.CharField(max_length=30)


class KpiMessage(models.Model):
    asset_id = models.CharField(max_length=30)
    attribute_id = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30)
    message_result = models.ManyToManyField(KpiInformation, through=KpiMessageEquationResult)
