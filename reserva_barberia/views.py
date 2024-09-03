from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

HORARIO = ["10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00"]

SERVICIOS = [{'servicio': 'Corte De Pelo', 'precio': '$20.000', "horario" : HORARIO}, {'servicio': 'Barba Al Raz + Toallas Calientes', 'precio': '$10.000', "horario" : HORARIO}, {'servicio': 'Corte Con Tijeras', 'precio': '$22.000',"horario" : HORARIO}, {'servicio': 'Corte Pelo y Barba + Lavado','precio': '$30.000',"horario" : HORARIO}]

reservas_barberia = []

def validar_horario(horario):
    return horario in HORARIO



def hora_ya_registrada(horario):
    for horario in SERVICIOS:
        if horario['horario']:
            return True
        return False

def crear_reserva(request):
            try:
                while True:
                    try:
                        rut = int(input("Ingrese su rut: "))
                    except ValueError:
                        print("Error, ingrese valores numericos para el RUT.")
                    else:
                        break
                nombre = input("Ingresa tu nombre: ")
                print("Servicios disponibles: ")
                for idx, servicio in enumerate(SERVICIOS):
                    print(f"{idx + 1}:{servicio["servicio"]}")
                servicio_idx = int(input("Elige un servicio (numero): "))
                servicio_seleccionado = SERVICIOS[servicio_idx] #mio

                for idx, hora in enumerate(HORARIO):
                    print(f"{idx + 1}:{hora}")
                hora_idx = int(input("Elige un servicio (numero): "))
                hora_seleccionada = HORARIO[hora_idx] #mio
                
            except Exception as e:
                print(f"Ha ocurrido un error {e}")    

            else:
                print("Boleto creado con exito, caya a la web")
                reservas = {
                    "rut" : rut,
                    "nombre": nombre,
                    "servicio": servicio_seleccionado,
                    "horario": hora_seleccionada
                }
                reservas_barberia.append(reservas)
            respuesta = f'''
            <httml>
            <body>
                <h1>Tu reserva</h1>
                <p> Rut : {rut} <br>
                <p> Nombre : {nombre} <br>
                <p> Servicio : {servicio_seleccionado['servicio']} <br>
                <p> Hora : {hora_seleccionada} <br>
            </body>
            </httml>
            '''
            return HttpResponse(respuesta)   