from django.db import models

# Create your models here.

class Usuarios(models.Model):
    USULOGIN=models.CharField(max_length=15)
    USUPASSWORD=models.CharField(max_length=15)

class Ciudades(models.Model):
    CIUCODIGO=models.IntegerField(max_length=6)
    CIUNOMBRE=models.CharField(max_length=10)

class Sucursales(models.Model):
    SUCCODIGO=models.IntegerField(max_length=6)
    CIUCODIGO=models.ForeignKey(Ciudades,on_delete=models.CASCADE)
    SUCNOMBRE=models.CharField(max_length=20)

class Tipocurso(models.Model):
    TIPCURCODIGO=models.IntegerField(max_length=6)
    TIPCURNOMBRE=models.CharField(max_length=20)
    TIPCURVALOR=models.IntegerField(max_length=11)

class Alumnos(models.Model):
    ALUMRUT=models.CharField(max_length=12)
    ALUMNOMBRE=models.CharField(max_length=15)
    ALUMAPATERNO=models.CharField(max_length=15)
    ALUMAMATERNO=models.CharField(max_length=15)
    ALUMDIRECCION=models.CharField(max_length=60)
    ALUMEMAIL=models.CharField(max_length=40)
    ALUMFONO=models.CharField(max_length=16)

class Matriculas(models.Model):
    MATNUMERO=models.IntegerField(max_length=11)
    TIPCURCODIGO=models.ForeignKey(Tipocurso,on_delete=models.CASCADE)
    ALUMRUT=models.ForeignKey(Alumnos,on_delete=models.CASCADE)
    SUCCODIGO=models.ForeignKey(Sucursales,on_delete=models.CASCADE)
    MATFECHA=models.DateField()



