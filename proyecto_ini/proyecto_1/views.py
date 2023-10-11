from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def index(request):
   doc_ext = open("./plantillas/index.html")
   plt = Template(doc_ext.read())   
   doc_ext.close()
   ctx=Context()
   rndr = plt.render(ctx)
   return HttpResponse(rndr)

def promedios(request):
   prod = open("./plantillas/promedios.html")
   plt = Template(prod.read())   
   prod.close()   


   num1 = float (request.GET["nota1"])
   num3 = float (request.GET["nota3"])
   num2 = float (request.GET["nota2"])
   num4 = float (request.GET["nota4"])
   num5 = float (request.GET["nota5"])
   num6 = float (request.GET["nota6"])
   promd = ((num1*0.15)+(num2 *0.15)+(num3*0.2)
   +(num4*0.2)+(num5*0.15)+(num6*0.15))

   ctx=Context({"N1":num1,"N2":num2,"N3":num3, "N4":num4,
   "N5":num5, "N6":num6, "promedio_final":promd})
   rndr = plt.render(ctx)
   return HttpResponse(rndr)