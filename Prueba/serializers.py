from rest_framework import serializers
from Prueba.models import Alumnos,Matriculas

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alumnos
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Matriculas
        fields = '__all__'