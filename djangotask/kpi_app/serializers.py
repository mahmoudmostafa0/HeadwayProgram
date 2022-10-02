from kpi_app.models import KpiDevice, KpiMessage, KpiMessageEquationResult, KpiInformation
from rest_framework import serializers


class KpiDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KpiDevice
        fields = ['asset_id', 'kpi_id']


class KpiInformationSerializer(serializers.ModelSerializer):
    assets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='asset_id')

    class Meta:
        model = KpiInformation
        fields = "__all__"


class KpiMessageEquationResultSerilizer(serializers.ModelSerializer):
    class Meta:
        model = KpiMessageEquationResult
        fields = ['value', 'kpi_equation']


class KpiMessageSerilizer(serializers.ModelSerializer):
    # assets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='asset_id')
   # message_result = KpiMessageEquationResultSerilizer(many=True, read_only=True)

    class Meta:
        model = KpiMessage
        fields = ['asset_id', 'attribute_id', 'timestamp']
