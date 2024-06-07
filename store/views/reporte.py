from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class Reporte:
    def reporte(request):
        reporte= Order.objects.filter(status=True)
        suma=0
        for s in reporte:
            suma+=s.price
        contexto={"reporte":reporte,'suma':suma}
        return render(request,'reporte.html',contexto)