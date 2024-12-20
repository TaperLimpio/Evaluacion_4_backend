"""
URL configuration for ProyectoBD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Prueba.views import Index_Ciudades,Create_Ciudad,View_Ciudad,Delete_Ciudad,Update_Ciudad

from Prueba.views import Index_Tipo_Curso,Create_tipocurso,View_tipocurso, actualizar_tipoCurso, delete_tipoCurso

from Prueba.views import Index_Alumnos,Create_Alumno,View_Alumno, actualizar_Alumno, delete_Alumno

from Prueba.views import login_view

from Prueba.views import Index_Usuario,View_Usuario,Update_Usuario

from Prueba.views import SucursalIndex,sucursalView,sucursalCreate, sucursalUpdate, sucursalDelete

from Prueba.views import matriculaIndex,matriculaCreate,matriculaView,matriculaUpdate,matriculaDelete

from Prueba.views import AlumnoCriterio,MatriculaFecha,MatriculaSucursal

from Prueba.views import Alumno_list,Alumno_details,Matricula_list,Matricula_details

from sitio.views import Index_Alumnos_api,Create_Alumno_api,View_Alumno_api,Update_Alumno_api
from sitio.views import Delete_Alumno_api

urlpatterns = [
    path('admin/', admin.site.urls),

    #Prueba

    #ciudad
    path('ciudades/',Index_Ciudades,name='Ciudades'),
    path('ingresar-ciudades/',Create_Ciudad),
    path('view-ciudades/<int:id>',View_Ciudad),
    path('delete-ciudad/<int:id>',Delete_Ciudad),
    path('actualizar-ciudad/<int:id>',Update_Ciudad),

    #Tipo Curso
    path('tipo cursos/',Index_Tipo_Curso),
    path('ingresar-tipos de curso/',Create_tipocurso),
    path('view-tipo curso/<int:id>',View_tipocurso),
    path('actualizar_tipoCurso/<int:id>', actualizar_tipoCurso),
    path('delete_tipoCurso/<int:id>', delete_tipoCurso),

    #Alumnos
    path('alumnos/',Index_Alumnos),
    path('ingresar-alumnos/',Create_Alumno),
    path('view-alumnos/<int:id>',View_Alumno),
    path('actualizar_Alumno/<int:id>', actualizar_Alumno),
    path('delete_Alumno/<int:id>', delete_Alumno),
    #Alumnos-api
    path('alumnos-API/',Alumno_list),
    path('alumnos-API/<int:pk>',Alumno_details),

    #login
    path('login/',login_view,name='login'),

    #sucursales
    path('sucursal/',SucursalIndex),
    path('ingresar-sucursal/',sucursalCreate),
    path('ver-sucursal/<int:id>',sucursalView),
    path('sucursalUpdate/<int:id>/', sucursalUpdate),
    path('sucursalDelete/<int:id>/', sucursalDelete),
 
    #Usuarios
    path('usuario/',Index_Usuario),
    path('view-usuario/<int:id>',View_Usuario),
    path('actualizar-usuario/<int:id>',Update_Usuario),

    #matriculas
    path('matriculas/',matriculaIndex),
    path('crear-matricula/',matriculaCreate),
    path('ver-matriculas/<int:id>',matriculaView),
    path('editar-matricula/<int:id>/', matriculaUpdate),
    path('eliminar-matricula/<int:id>/',matriculaDelete),
    #Matriculas-api
    path('matriculas-API/',Matricula_list),
    path('matriculas-API/<int:pk>',Matricula_details),

    #Busquedas por criterios
    path('Alumnos-criterios/',AlumnoCriterio,name='Alumnos-criterios'),
    path('Matriculas-fecha/',MatriculaFecha,name='Matriculas-fecha'),
    path('Matriculas-sucursal/',MatriculaSucursal,name="Matriculas-sucursal"),

    #INTERFAZ DE CONSUMO DE APIS
    path('alumnos-index/',Index_Alumnos_api),
    path('alumnos-create/',Create_Alumno_api,name="alumnos_create"),
    path('alumnos-view/<int:id>',View_Alumno_api,name="alumnos_view"),
    path('alumnos-update/<int:id>',Update_Alumno_api,name="alumnos_update"),
    path('alumnos-delete/<int:id>',Delete_Alumno_api,name="alumnos_delete"),
]
