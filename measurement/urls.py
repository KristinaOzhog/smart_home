from django.urls import path

from measurement.views import SensorView, MeasurementView, AllSensorsView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('allsensors/', AllSensorsView.as_view()),
]
