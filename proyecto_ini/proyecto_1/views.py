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
   ctx=Context()
   rndr = plt.render(ctx)
   return HttpResponse(rndr)
   
def calc_prom(request):
      num1 = "La nota 1 es :%r" %request.GET['nota1']
      return HttpResponse (num1)