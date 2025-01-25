from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from CRUD.models import Chicken
from CRUD.serializers import FarmSerializer


# Create your views here.

class FarmView(APIView):
    def get(self, request):
        data=Chicken.objects.all()####
        serialized_data = FarmSerializer(data, many=True)
        return Response(status=status.HTTP_200_OK,data=serialized_data.data)

    def post(self, request):
        data=request.data
        serializer= FarmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_210_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChickenUpdate(APIView):
    def get(self,request, pk):
        chicken = Chicken.object.get(pk=pk)
        serialized_data = FarmSerializer(chicken)
        return Response(status=status.HTTP_200_OK, data=serialized_data.data)


class SingleChickenView(APIView):
    def get(self, request, pk):
        try:
            chicken = Chicken.objects.get(pk=pk)
            serialized_data = FarmSerializer(chicken)
            return Response(status=status.HTTP_200_OK, data=serialized_data.data)
        except Chicken.DoesNotExist:
            return Response(status= status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk):
        chicken= Chicken.objects.get(pk=pk)
        serialized_data = FarmSerializer(chicken, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return  Response (status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        chicken= Chicken.objects.get(pk=pk)
        seriazlized_data = FarmSerializer(chicken, data=request.data,parial=True)
        if seriazlized_data.is_valid():
            seriazlized_data.save()
            return Response(status=status.HTTP_200_OK)
        return Response(seriazlized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            chicken = Chicken.object.get(pk=pk)
            chicken.delete()
            return Response(status=status.HTTP_200_OK)
        except Chicken.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
