from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import  TemplateView
from django.urls import  reverse_lazy
from .forms import Report_Form
from app.orders.models import OrderItem
from app.servicios.models import *
from datetime import datetime
# Create your views here.
from ..servicios.models import Product
from ..denuncias.models import  Denuncias
from ..adopciones.models import Perros,Solicitudes
from ..donaciones.models import Solicitudes as Soli,Productos
class reportGrafico(TemplateView):
    model = Product
    template_name = 'Reportes/Reporte_grafico.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_grafico':
                data = {
                    'name': 'Cantidad',
                    'colorByPoint':True,
                    'data': self.get_grafico(),
                }

            else:
                data['error'] = 'ha ocurrido un error'
            # data = Product.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = data
            # print(Product.objects.get(pk=request.POST['id']))
            # print(request.POST)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)
    def get_grafico(self):
        data=[]
        try:
            year = datetime.now().year
            for p in Product.objects.all():

                    # Order2 = Order.objects.filter(id=Order1.id)
                data.append({
                     'name': p.name,
                     'y':float(p.stock),
                }
                )
        except:
            pass
        return data



    def get_context_data(self, **kwargs):
        context=super(reportGrafico, self).get_context_data(**kwargs)
        context['title']='Reporte de ventas'
        context['entity']="Despliegue de reportes de ventas"
        context['list_url']=reverse_lazy('reportes_ventas')
        context['get_grafico']=self.get_grafico()
        context['form'] = Report_Form()
        return context

class reporteProductos(TemplateView):
    model = Product

    template_name = 'Reportes/reportes_productos.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Product.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(created__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.name,
                        s.created.strftime('%Y-%m-%d'),
                        s.slug,
                        s.description,
                        s.price,
                        s.stock,
                    ])
            elif action == 'get_grafico':
                        data = {
                            'name': 'Cantidad',
                            'colorByPoint': True,
                            'data': self.get_grafico(),
                        }
            else:
                data['error'] = 'ha ocurrido un error'

            # data = Product.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = data
            # print(Product.objects.get(pk=request.POST['id']))
            # print(request.POST)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_grafico(self):
        data = []
        try:
            year = datetime.now().year
            for p in Product.objects.all():
                # Order2 = Order.objects.filter(id=Order1.id)
                data.append({
                    'name': p.name,
                    'y': float(p.stock),
                }
                )
        except:
            pass
        return data
    def get_context_data(self, **kwargs):
        context=super(reporteProductos, self).get_context_data(**kwargs)
        context['title']='Reporte de ventas'
        context['entity']="Despliegue de reportes de ventas"
        context['list_url']=reverse_lazy('reportes_ventas')
        context['form'] = Report_Form()
        return context

class reportVentas(TemplateView):
    template_name = 'Reportes/Reportes_ventas.html'


    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        data= {}
        try:
            action=request.POST['action']
            if action =='search_report':
                data=[]
                start_date=request.POST.get('start_date','')
                end_date= request.POST.get('end_date','')
                search=OrderItem.all()
                if len(start_date) and len(end_date):
                    search =search.filter(date_joined_range=[start_date,end_date])
                for s in search:
                    data.append([
                        s.order,
                        s.product,
                        s.price,
                        s.quantity
                    ])
            else:
                data['error']='Ha ocurrido un error'
        except Exception as e:
            return  JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context=super(reportVentas, self).get_context_data(**kwargs)
        context['title']='Reporte de ventas'
        context['entity']="Despliegue de reportes de ventas"
        context['list_url']=reverse_lazy('reportes_ventas')
        context['form'] = Report_Form()
        return context

#REPORTE DE DENUNCIAS ::
class reportDenuncia(TemplateView):
    model = Denuncias

    template_name = 'Reportes/Denuncias/reporte_denuncia.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Denuncias.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_creacion__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.nombres,
                        s.fecha_creacion.strftime('%Y-%m-%d'),
                        s.cedula,
                        s.telefono,
                        s.direccion,
                        s.descripcion,
                    ])
            elif action == 'get_grafico':

                data = {
                    'name': 'Cantidad',
                    'colorByPoint': True,
                    'data': self.get_grafico(),
                }
            else:
                data['error'] = 'ha ocurrido un error'

            # data = Product.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = data
            # print(Product.objects.get(pk=request.POST['id']))
            # print(request.POST)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_grafico(self):
        data = []
        try:
            stock = 20
            year = datetime.now().year

            #for m in range(1,13):
            for p in Denuncias.objects.all():
                # Order2 = Order.objects.filter(id=Order1.id)
               # stock=Denuncias.objects.filter(fecha_creacion__year=year,Denuncias_id=p.id).aggregate(p.id)
                data.append({
                    'name': p.nombres,
                    'y': float(year),
                })

            return data
        except:
            pass

    def get_context_data(self, **kwargs):
        context=super(reportDenuncia, self).get_context_data(**kwargs)
        context['title']='Reporte de Denuncias'
        context['entity']="Despliegue de reportes de Denuncias"
        context['list_url']=reverse_lazy('reportes_Denuncia')
        context['form'] = Report_Form()
        return context


#REPORTE ADOPCIONES :
class reportAdopciones(TemplateView):
    model =Solicitudes

    template_name = 'Reportes/Denuncias/reporte_denuncia.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Solicitudes.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.date_joined.strftime('%Y-%m-%d'),
                        s.id,
                        s.nombre,
                        s.apellido,
                        s.cedula,
                        s.direccion,
                        s.descripcion,
                        s.perros.nombre,
                    ])
            elif action == 'get_grafico':

                data = {
                    'name': 'Cantidad',
                    'colorByPoint': True,
                    'data': self.get_grafico(),
                }
            else:
                data['error'] = 'ha ocurrido un error'

            # data = Product.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = data
            # print(Product.objects.get(pk=request.POST['id']))
            # print(request.POST)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_grafico(self):
        data = []
        try:
            stock = 20
            year = datetime.now().year

            #for m in range(1,13):
            for p in Solicitudes.objects.all():
                # Order2 = Order.objects.filter(id=Order1.id)
               # stock=Denuncias.objects.filter(fecha_creacion__year=year,Denuncias_id=p.id).aggregate(p.id)
                data.append({
                    'name': p.nombres,
                    'y': float(year),
                })

            return data
        except:
            pass

    def get_context_data(self, **kwargs):
        context=super(reportAdopciones, self).get_context_data(**kwargs)
        context['title']='Reporte de Adocpiones'
        context['entity']="Despliegue de reportes de Adopciones"
        context['list_url']=reverse_lazy('reporte_adopciones')
        context['form'] = Report_Form()
        return context
#REPORTE DONACIONES :
class reportDonaciones(TemplateView):
    model =Soli
    template_name = 'Reportes/Denuncias/reporte_denuncia.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Soli.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.date_joined.strftime('%Y-%m-%d'),
                        s.id,
                        s.nombre,
                        s.apellido,
                        s.cedula,
                        s.telefono,
                        s.email,
                        s.descripcion,
                        s.productos.nombre,
                    ])
            elif action == 'get_grafico':

                data = {
                    'name': 'Cantidad',
                    'colorByPoint': True,
                    'data': self.get_grafico(),
                }
            else:
                data['error'] = 'ha ocurrido un error'

            # data = Product.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = data
            # print(Product.objects.get(pk=request.POST['id']))
            # print(request.POST)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_grafico(self):
        data = []
        try:
            stock = 20
            year = datetime.now().year

            #for m in range(1,13):
            for p in Soli.objects.all():
                # Order2 = Order.objects.filter(id=Order1.id)
               # stock=Denuncias.objects.filter(fecha_creacion__year=year,Denuncias_id=p.id).aggregate(p.id)
                data.append({
                    'name': p.nombres,
                    'y': float(year),
                })

            return data
        except:
            pass

    def get_context_data(self, **kwargs):
        context=super(reportDonaciones, self).get_context_data(**kwargs)
        context['title']='Reporte de Donaciones'
        context['entity']="Despliegue de reportes de Adopciones"
        context['list_url']=reverse_lazy('reporte_adopciones')
        context['form'] = Report_Form()
        return context