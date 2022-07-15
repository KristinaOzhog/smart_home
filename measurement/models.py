from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показания'






