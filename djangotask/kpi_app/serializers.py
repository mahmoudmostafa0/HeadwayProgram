from kpi_app.models import KpiInformation, KpiResult, KpiMessage
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = KpiMessage
        fields = "__all__"


class KpiInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KpiInformation
        fields = "__all__"


class KpiResultSerializer(serializers.ModelSerializer):
    result = serializers.CharField(max_length=50, read_only=True)
    message_kpi_expression = serializers.PrimaryKeyRelatedField(many=False, queryset=KpiInformation.objects.all())

    class Meta:
        model = KpiResult
        fields = "__all__"
