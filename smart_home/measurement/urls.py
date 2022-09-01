from django.urls import path
from .views import SensorListOrCreate, SensorInfoOrDescriptionChange, MeasurmentsAdd

urlpatterns = [
    path('sensors/', SensorListOrCreate.as_view()),
    path('sensors/<pk>/', SensorInfoOrDescriptionChange.as_view()),  # подключаем маршруты из приложения measurement
    path("measurements/", MeasurmentsAdd.as_view())
]
