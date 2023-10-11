from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
   doc_ext = open("./plantillas/index.html")
   plt = Template(doc_ext.read())   
   doc_ext.close()
   ctx=Context()
   rndr = plt.render(ctx)
   return HttpResponse(rndr)

@csrf_exempt
def promedios(request):
   
   prod = open("./plantillas/promedios.html")
   plt = Template(prod.read())   
   prod.close()   
   # creo que aprendi bastante en la prueba :D
   #esta fue la parte mas desafiante, pero estuvo entretenido 
   num1 = float (request.GET["nota1"])
   num3 = float (request.GET["nota3"])
   num2 = float (request.GET["nota2"])
   num4 = float (request.GET["nota4"])
   num5 = float (request.GET["nota5"])
   num6 = float (request.GET["nota6"])
   #esta parte fue bastante interesante 
   promd = round((num1*0.15)+(num2 *0.15)+(num3*0.2)
   +(num4*0.2)+(num5*0.15)+(num6*0.15), 1)
   nomb = str(request.GET["nom_est"])
   run = str (request.GET["run_est"])
   carr = str(request.GET["Carrera"]) 
   #podria poner un if - else, para verificar que los valores no esten vacios pero tengosueño C:

   ctx=Context({"N1":num1,"N2":num2,"N3":num3, "N4":num4,
   "N5":num5, "N6":num6, "promedio_final":promd,"nombre_al":nomb,
   "Run":run, "Carrera":carr})
   rndr = plt.render(ctx)

   return HttpResponse(rndr)