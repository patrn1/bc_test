from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from risks.models import *
from risks.serializers import *

@api_view(['GET'])

def get_risk_type(request, id):
    fields = RiskType.objects.filter(id=id)

    serializer = RiskTypeSerializer(fields, many=True, context={'request': request})

    return JsonResponse(serializer.data, safe=False)

def get_risk_types(request):

    fields = RiskType.objects.all()

    serializer = RiskTypeSerializer(fields, many=True, context={'request': request})

    return JsonResponse(serializer.data, safe=False)
