from rest_framework.test import APITestCase
from django.http import JsonResponse
from rest_framework import status 
from django.urls import reverse
from risks.models import *

class RiskTypesTests(APITestCase):

    def setUp(self):
        auto_risk_type = RiskType.objects.create(id="1", name="automobiles")
        houses_risk_type = RiskType.objects.create(id="2", name="houses")
        text_type = DataType.objects.create(id="1", name="text")
        num_type = DataType.objects.create(id="2", name="number")
        enum_type = DataType.objects.create(id="4", name="enum")
        date_type = DataType.objects.create(id="3", name="date")
        RiskTypeField.objects.create(
            id="4", 
            name="fuel", 
            description="field4_desc",
            risk_type=auto_risk_type,
            data_type=enum_type,
            properties="{'options':[ 'diesel', 'petrol']}"
        )
        RiskTypeField.objects.create(
            id="3", 
            name="manufacture_date", 
            description="field3_desc",
            risk_type=auto_risk_type,
            data_type=date_type
        )
        RiskTypeField.objects.create(
            id="2", 
            name="mileage",
            description="field2_desc",
            risk_type=auto_risk_type,
            data_type=num_type
        )
        RiskTypeField.objects.create(
            id="1", 
            name="model", 
            description="field1_desc",
            risk_type=auto_risk_type,
            data_type=text_type
        )
        RiskTypeField.objects.create(
            id="5", 
            name="address", 
            description="field5_desc",
            risk_type=houses_risk_type,
            data_type=text_type
        )


    def test_get_one_type(self):
        """
        Ensure we can get data about specific risk type.
        """
        response = self.client.get(reverse('get_risk_type', kwargs={'id':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            self.type_data
        )

    def test_get_all_types(self):
        """
        Ensure we can get data about all risk types.
        """
        response = self.client.get(reverse('get_risk_types'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            self.types_data
        )

    type_data = [
        {
            "id":1,
            "fields" : [
                {  
                   "id":1,
                   "data_type":{  
                       "id":1,
                       "name":"text",
                       "description":None
                   },
                   "risk_type":1,
                   "name":"model",
                   "description":"field1_desc",
                   "properties":None
                },
                {  
                    "id":2,
                    "data_type":{  
                       "id":2,
                       "name":"number",
                       "description":None
                    },
                    "risk_type":1,
                    "name":"mileage",
                    "description":"field2_desc",
                    "properties":None
                },
                {
                    "id":3,
                    "data_type":{  
                       "id":3, 
                       "name":"date",
                       "description":None
                    },
                    "risk_type":1,
                    "name":"manufacture_date",
                    "description":"field3_desc",
                    "properties":None
                },
                {  
                    "id":4,
                    "data_type":{  
                       "id":4,
                       "name":"enum",
                       "description":None
                    },
                    "risk_type":1,
                    "name":"fuel",
                    "description":"field4_desc",
                    "properties":"{'options':[ 'diesel', 'petrol']}"
                }
            ],
            "name":"automobiles",
            "description":None
        }

    ]

    types_data = type_data + [{
        "id":2,
        "fields" : [{
            "id":5,
            "data_type":{
               "id":1,
               "name":"text",
               "description":None
            },
            "risk_type":2,
            "name":"address",
            "description":"field5_desc",
            "properties":None
        }],
        "name":"houses",
        "description":None
    }]