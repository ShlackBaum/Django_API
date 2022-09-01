# TODO: опишите необходимые обработчики через ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

class SensorListOrCreate(ListAPIView, CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        queryset = Sensor.objects.create(
            name="Имя счетчика",
            description="Описание счетчика"
        )
        serializer_class = SensorSerializer
        return HttpResponse("Сенсор создан")

class SensorInfoOrDescriptionChange(RetrieveAPIView, RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        queryset = Sensor.objects.filter(pk=pk).update(description="Измененное описание 888")
        serializer_class = SensorSerializer
        return Response(f"""Описание элемента с ID {pk} изменено""")

# Добавление измерения POST с указанием счетчика и температуры:
class MeasurmentsAdd(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        queryset = Measurement.objects.create(
            temp="30",
            sensor=Sensor.objects.get(id=20))
        serializer_class = SensorSerializer
        return Response(f"""Температура добавлена""")
