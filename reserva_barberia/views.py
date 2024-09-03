from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

HORARIO = ["10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00"]

RESERVA = [{'servicio': 'Corte De Pelo', 'precio': '$20.000', "horarios" : HORARIO}, {'servicio': 'Barba Al Raz + Toallas Calientes', 'precio': '$10.000', "horarios" : HORARIO}, {'servicio': 'Corte Con Tijeras', 'precio': '$22.000',"horarios" : HORARIO}, {'servicio': 'Corte Pelo y Barba + Lavado','precio': '$30.000',"horarios" : HORARIO}]