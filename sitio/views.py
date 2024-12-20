from django.shortcuts import render
from django.http import JsonResponse
import requests
from .forms import AlumnosForm

API_URL = "http://127.0.0.1:8000/alumnos-API"
def Index_Alumnos_api(request):
    return render(request,"Alumnos/index.html")

def Create_Alumno_api(request):
    form = AlumnosForm()
    if request.method == "POST":
        alurut = request.POST.get("ALUMRUT")
        alunombre = request.POST.get("ALUMNOMBRE")
        aluapaterno = request.POST.get("ALUMAPATERNO")
        aluamaterno = request.POST.get("ALUMAMATERNO")
        aludireccion = request.POST.get("ALUMDIRECCION")
        aluemail = request.POST.get("ALUMEMAIL")
        alufono = request.POST.get("ALUMFONO")

        payload = {
            "ALUMRUT":alurut,
            "ALUMNOMBRE":alunombre,
            "ALUMAPATERNO":aluapaterno,
            "ALUMAMATERNO":aluamaterno,
            "ALUMDIRECCION":aludireccion,
            "ALUMEMAIL":aluemail,
            "ALUMFONO":alufono
        }
        print(payload)

        response = requests.post(f"{API_URL}/", json=payload)

        if response.status_code == 201:
            return render(request,'Alumnos/index.html')
        else:
            return JsonResponse({"message": "Error al Crear al Alumno"}, status=response.status_code)
    data={'form':form}
    return render(request,'Alumnos/create.html',data)

def View_Alumno_api(request, id):
    api_url = f"{API_URL}/{id}"
    response = requests.get(api_url)
    alumno = response.json() if response.status_code == 200 else None
    return render(request, 'Alumnos/view.html', {'alumno':alumno})

def Update_Alumno_api(request, id):
    if request.method == "POST":
        aluid = request.POST.get("id")
        alurut = request.POST.get("rut")
        alunombre = request.POST.get("nombre")
        aluapaterno = request.POST.get("apaterno")
        aluamaterno = request.POST.get("amaterno")
        aludireccion = request.POST.get("direccion")
        aluemail = request.POST.get("email")
        alufono = request.POST.get("fono")

        payload = {
            "id":aluid,
            "ALUMRUT":alurut,
            "ALUMNOMBRE":alunombre,
            "ALUMAPATERNO":aluapaterno,
            "ALUMAMATERNO":aluamaterno,
            "ALUMDIRECCION":aludireccion,
            "ALUMEMAIL":aluemail,
            "ALUMFONO":alufono
        }

        response = requests.put(f"{API_URL}/{id}", json=payload)

        if response.status_code == 200:
             return render(request,"Alumnos/index.html")
        else:
            return JsonResponse({"message": "Error al actualizar al alumno"}, status=response.status_code)
        
    api_url = f"{API_URL}/{id}"
    response = requests.get(api_url)
    alumno = response.json() if response.status_code == 200 else None
    return render(request, 'Alumnos/edit.html', {'alumno':alumno})

def Delete_Alumno_api(request,id):
    if request.method == "POST":
        aluid=request.POST.get("id")
        payload = {
            "id":aluid
        }
        response = requests.delete(f"{API_URL}/{id}", json=payload)

        if response.status_code == 204:
             return render(request,"Alumnos/index.html")
        else:
            return JsonResponse({"message": "Error al Eliminar al alumno"}, status=response.status_code)

    api_url = f"{API_URL}/{id}"
    response = requests.get(api_url)
    print(response)
    alumno = response.json() if response.status_code == 200 else None
    return render(request, 'Alumnos/delete.html', {'alumno':alumno})