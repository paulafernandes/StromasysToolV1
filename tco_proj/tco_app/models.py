from django.db import models

# Create your models here.
class SystemTable(models.Model):
    system_name = models.CharField(max_length=50)

class ModelTable(models.Model):
    model_name = models.CharField(max_length=50)
    power_name = models.CharField(max_length=50)
    power_watt = models.IntegerField(default=0)    
    id_system = models.ForeignKey(SystemTable, on_delete=models.CASCADE)

class LicenceTable(models.Model):
    licence_name = models.CharField(max_length=50)
    licence_cost = models.IntegerField(default=0)

class CpuTable(models.Model):
    min_cpu = models.IntegerField(default=0)
    max_cpu = models.IntegerField(default=0)
    id_model = models.ForeignKey(ModelTable, on_delete=models.CASCADE)
    id_licence = models.ForeignKey(LicenceTable, on_delete=models.CASCADE)
