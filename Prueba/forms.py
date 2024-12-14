from django import forms 
from Prueba.models import Ciudades,Tipocurso,Alumnos,Usuarios



class CiudadesForm(forms.ModelForm):
    class Meta:
        model=Ciudades
        fields='__all__'

class TipoCursoForm(forms.ModelForm):
    class Meta:
        model=Tipocurso
        fields='__all__'

class AlumnosForm(forms.ModelForm):
    class Meta:
        model=Alumnos
        fields='__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuarios
        fields='__all__'
        

