from rest_framework import serializers

from risks.models import *

class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = '__all__'

class RiskTypeFieldSerializer(serializers.ModelSerializer):
    data_type = DataTypeSerializer()

    class Meta:
        model = RiskTypeField
        fields = '__all__'

class RiskTypeSerializer(serializers.ModelSerializer):
    fields = RiskTypeFieldSerializer(source='risktypefield_set', many=True)

    class Meta:
        model = RiskType
        fields = '__all__'