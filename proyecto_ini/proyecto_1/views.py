from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
   
   return render(request, "index.html")

@csrf_exempt
def promedios(request):
   # creo que aprendi bastante en la prueba :D
   #esta fue la parte mas desafiante, pero estuvo entretenido 
   num1 = float(request.POST["nota1"])
   num3 = float(request.POST["nota3"])
   num2 = float(request.POST["nota2"])
   num4 = float(request.POST["nota4"])
   num5 = float(request.POST["nota5"])
   num6 = float(request.POST["nota6"])
   #esta parte fue bastante interesante 
   promd = round((num1*0.15)+(num2 *0.15)+(num3*0.2)
   +(num4*0.2)+(num5*0.15)+(num6*0.15), 1)
   nomb = str(request.POST["nom_est"])
   run = str (request.POST["run_est"])
   carr = str(request.POST["Carrera"]) 
   mod = str (request.POST["modulo"])
   #podria poner un if - else, para verificar que los valores no esten vacios pero tengosueño C:

   return render( request, "promedios.html",{"N1":num1,"N2":num2,"N3":num3, "N4":num4,
   "N5":num5, "N6":num6, "promedio_final":promd,"nombre_al":nomb,
   "Run":run, "Carrera":carr,"mod":mod,})

"""   
@csrf_exempt
def promedios(request):
   wea='esta es %s' %request.POST['nom_est']
   return HttpResponse(wea)
"""