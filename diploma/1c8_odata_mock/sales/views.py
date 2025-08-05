from django.shortcuts import render
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import SalesRequestSerializer, SalesResponseSerializer
import xml.etree.ElementTree as ET
import xml.dom.minidom
from datetime import datetime

class SalesAPIView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):

        serializer = SalesRequestSerializer(data=request.data)

        if serializer.is_valid():

            type_sale = serializer.validated_data['type_sale']
            contract = serializer.validated_data['contract']

            def dict_to_xml(tag, dictionary):

                element = ET.Element(tag)

                for key, val in dictionary.items():
                    child = ET.SubElement(element, key)
                    child.text = str(val)

                return element

            def pretty_xml(xml_str):

                dom = xml.dom.minidom.parseString(xml_str)

                return dom.toprettyxml(indent="  ")

            contract_xml_element = dict_to_xml("contract", contract)
            contract_xml_str = ET.tostring(contract_xml_element, encoding='unicode', method='xml')
            xml_pretty = pretty_xml(contract_xml_str)

            xml_string = f"<?xml version='1.0'?><input_params>{xml_pretty}</input_params>"
            sale_date = datetime.now().strftime("%Y-%m-%d")

            response_data = {
                "status": "OK",
                "contract": contract,
                "xml": xml_string,
                "sale": {"date": sale_date}
            }

            response_serializer = SalesResponseSerializer(response_data)

            return Response(response_serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
