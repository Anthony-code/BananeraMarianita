import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic.base import View
from xhtml2pdf import pisa
from ControlPersonal.models import Persona, Cuenta, Proveedor

def templeteReportProovedor(request):
    templete_name = 'reporte-template/reporte-proovedor.html'
    context ={}
    if request.method == 'GET':
        context = {}
    return render(request, templete_name)


class viewReportProovedor(LoginRequiredMixin,View):
    print("aa")
    def get(self,request, *args, **kwargs):

        try:
            template = get_template('reporte/reporte_proovedor.html')## SE CAPTURA EL TEMPLETE QUE SE VA A UTILIZAR
            q = request.GET.get("estado") ##SE RECUPERA EL VALOR DEL HTML QUE SE BUSCA
            if q == "general":
                proovedor = Proveedor.objects.all()
            else:
                if not q:
                    proovedor = Proveedor.objects.all()
                else:
                    proovedor = Proveedor.objects.filter(estado=q)

            fecha = timezone.now()
            ##EL CONTEXT PARA GENERAR LOS DATOS CORRESPONDIENTE PARA QUE SE PUEDA ENVIAR
            context ={
                'proovedor':proovedor,
                'fecha':fecha,
                'request':request
            }
            response = HttpResponse(content_type="application/pdf")  ###QUE TIPO DE CONTEXTO SE LE ENVIA EN ESTE CASO
            ##LA APLICACION ES PARA PDF POR ESA SITUACION SE MANDA CON PARAMETRO "application/pdf"

            ###QUE TIPO DE PDF SE LE ENVIA ... SE ESPESICICA SI SE MUESTRA EN UNA PESTAÑA NUEVA
            ###O QUIERE SER DESCARGADO DIRECTAMENTE.

            response['Content-Disposition'] = 'inline; filename = reporte_proovedo_activo'
            ### EL FILEMANE ES PARA EL NOMBRE DEL ARCHIVO PD
            html = template.render(context)  ### creamos una variable que va tener un objeto del templete para ser rendirizado
            ### con la varibles de context que se definieron antes.
            pisaStatus = pisa.CreatePDF(html, dest=response)
            return response
        except:
            pass
        return  HttpResponseRedirect(reverse_lazy('ControlPersonal:lista_proovedor'))


class viewReportEmpleado(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        print("droga")
        # try:
        template = get_template('reporte/reporte_empleado.html')
        empleado = Persona.objects.all()
        fecha = timezone.now()
        context = {
            'empleado': empleado,
            'fecha': fecha,
            'request': request
        }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename = Nomina de empleados'
        html = template.render(context)
        pisa.CreatePDF(html, dest=response)
        return response
    # except:
    #     print("visio")
    #     pass

    # return HttpResponseRedirect(reverse_lazy('ControlPersonal:lista_empleado'))
