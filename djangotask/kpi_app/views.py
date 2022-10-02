# import sys
# sys.path.append('../interpreter')
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response

from interpreter import Compiler
# from Compiler.Tables.variables import Variables
# from kpi_app.models import KpiInformation, KpiDevice
# from kpi_app.serializers import KpiInformationSerializer, KpiDeviceSerializer

from kpi_app.models import KpiDevice, KpiInformation, KpiMessageEquationResult
from kpi_app.serializers import KpiInformationSerializer, KpiDeviceSerializer, KpiMessageSerilizer, \
    KpiMessageEquationResultSerilizer
from interpreter.Compiler import interpreter
from interpreter.Compiler.Tables.variables import Variables


# Create your views here.
@api_view(['POST'])
def send_message(request):
    """ send the message as json
    example '{"asset_id": "123", "attribute_id": "#", "timestamp": "2022-07-31T23:28:37Z[UTC]", "value": 1}'"""
    message_value = request.data['value']
    message_asset_id = request.data['asset_id']
    kpis_to_perform = [x.kpi_id for x in KpiDevice.objects.filter(
        asset_id=message_asset_id)]  # get all kpis that work for this device
    msg_serilizer = KpiMessageSerilizer(data=request.data)
    if msg_serilizer.is_valid():
        msg = msg_serilizer.save()
    resp = msg_serilizer.data
    results = []
    for kpi in kpis_to_perform:
        Variables.add_or_update("ATTR", message_value)
        message_result = KpiMessageEquationResult(kpi_equation=kpi, kpi_message=msg,
                                                  value=Compiler.interpreter.interpret_kpi(kpi.expression))
        message_result.save()
        result_serilizer = KpiMessageEquationResultSerilizer(message_result)
        results.append(result_serilizer.data)
        # result.append(
        #    {'kpi_name': kpi.name, 'value': interpreter.Compiler.interpreter.interpret_kpi(kpi.expression)})
        # request.data['value'] = result
    #resp = KpiMessageSerilizer(msg)
    #print(msg_serilizer.data)
    resp["result"] = results
    return Response(resp)


class KpiInformationController(ListCreateAPIView):
    """
    API endpoint that allows kpi resuts to be viewed or edited.
    """
    queryset = KpiInformation.objects.all()
    serializer_class = KpiInformationSerializer


class KpiDeviceController(ListCreateAPIView):
    """
    API endpoint that allows kpi resuts to be viewed or edited.
    """
    queryset = KpiDevice.objects.all()
    serializer_class = KpiDeviceSerializer
