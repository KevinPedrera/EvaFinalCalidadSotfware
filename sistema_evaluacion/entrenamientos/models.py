from django.db import models

class Rutina(models.Model):
    nombre = models.CharField(max_length=255)
    grupo_muscular = models.CharField(max_length=255)
    series = models.IntegerField()
    repeticiones = models.IntegerField()

    def __str__(self):
        return self.nombre