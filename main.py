from persona import Persona
from zapatilla import Zapatilla
from factura import Factura
from factura_detalle import FacturaDetalle
"""from reportlab.pdfgen import canvas"""
from tkinter import *

personas: Persona = []
zapatillas: Zapatilla = []
factutas: Factura = []



def persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)


def listar_personas():
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para editar persona: "))
    for persona in personas:
        if persona.dni == dni:
            continu: bool = True

            while continu:
                continu=int(input ("1 para EDITAR y 2 para SALIR: "))
                if continu == 1 :
                    print ("****************************************")
                    print ("*EDITAR PERSONA**********************")
                    print("                                         ")
                    print("===================MENÚ==================")
                    print("**************INGRESE OPCIONES***********")
                    print ("         1: PARA EDITAR NOMBRE         ")
                    print ("         2: PARA EDITAR APELLIDO         ")
                    print ("         3: PARA EDITAR DIRECCION           ")
                    print ("         4: PARA EDITAR TELEFONO          ")
                    print ("         10: PARA SALIR                 ")
                    print ("****************************************")
                    casos: str = str(input("INGRESE OPCIÓN: "))
                    match casos:  
                        case "1": 
                            persona.nombre = str(input("Ingrese nuevo nombre: "))
                        case "2":
                            persona.apellido = str(input("Ingrese nuevo apellido: "))
                        case "3":
                            persona.direccion = str(input("Ingrese nueva direccion: "))
                        case "4":
                            persona.telefono = str(input("Ingrese nuevo telefono: "))
                        case "6":
                            persona.nombre = str(input("Ingrese nuevo nombre: "))
                            persona.apellido = str(input("Ingrese nuevo apellido: "))
                            persona.direccion = str(input("Ingrese nueva direccion: "))
                            persona.telefono = str(input("Ingrese nuevo telefono: "))
                        case "10":
                            continu=False
                else:
                    continu = False


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para eliminar persona: "))
    for indice, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(indice)


def zapatilla():
    codigo: str = str(input("Ingrese código del zapatilla: "))
    precio: float = float(input("Ingrese precio del zapatilla: "))
    marca: str = str(input("Ingrese marca del zapatilla: "))
    talla: float = float(input("Ingrese la talla de la zapatilla: "))
    color: str = str(input("Ingrese el color de la zapatilla: "))
    actividad: str = str(input("Ingrese para que se usara la zapatilla: "))
    zapatilla: Zapatilla = Zapatilla(codigo, precio, marca, talla, color, actividad)
    zapatillas.append(zapatilla)


def listar_zapatilla():
    for zapatilla in zapatillas:
        Zapatilla.convertir_a_string(zapatilla)


def buscar_zapatilla():
    codigo: str = str(input("Ingrese Código para buscar la zapatilla: "))
    for zapatilla in zapatillas:
        if zapatilla.codigo == codigo:
            Zapatilla.convertir_a_string(zapatilla)
            return zapatilla

def editar_zapatilla():
    codigo: str = str(input("Ingrese codigo para editar zapatilla: "))
    for zapatilla in zapatillas:
        if zapatilla.codigo == codigo: 
            continua: bool = True

            while continua:
                continua=int(input ("1 para EDITAR y 2 para SALIR: "))
                if continua == 1 :
                    print ("****************************************")
                    print ("*EDITAR ZAPATILLAS**********************")
                    print("                                         ")
                    print("===================MENÚ==================")
                    print("**************INGRESE OPCIONES***********")
                    print ("         1: PARA EDITAR PRECIO          ")
                    print ("         2: PARA EDITAR MARCA           ")
                    print ("         3: PARA EDITAR TALLA           ")
                    print ("         4: PARA EDITAR COLOR           ")
                    print ("         5: PARA EDITAR NUEVA ACTIVIDAD ")
                    print ("         6: PARA EDITAR TODO            ")
                    print ("         10: PARA SALIR                 ")
                    print ("****************************************")
                    casos: str = str(input("INGRESE OPCIÓN: "))
                    match casos:  
                        case "1": 
                            zapatilla.precio = str(input("Ingrese nuevo precio: "))
                        case "2":
                            zapatilla.marca = str(input("Ingrese nueva marca: "))
                        case "3":
                            zapatilla.talla = str(input("Ingrese nueva talla: "))
                        case "4":
                            zapatilla.color = str(input("Ingrese nuevo color: "))
                        case "5":
                            zapatilla.actividad = str(input("Ingrese nueva actividad: "))
                        case "6":
                            zapatilla.precio = str(input("Ingrese nuevo precio: "))
                            zapatilla.marca = str(input("Ingrese nueva marca: "))
                            zapatilla.talla = str(input("Ingrese nueva talla: "))
                            zapatilla.color = str(input("Ingrese nuevo color: "))
                            zapatilla.actividad = str(input("Ingrese nueva actividad: "))
                        case "10":
                            continua=False
                else:
                    continua = False
            
def eliminar_zapatilla():
    codigo: str = str(input("Ingrese codigo para eliminar zapatilla: "))
    for indice, zapatilla in enumerate(zapatillas):
        if zapatilla.codigo == codigo:
            zapatillas.pop(indice)



def nueva_factura():
    print("para generar una factura busca un cliente")
    cliente: Persona = buscar_persona()
    factura: Factura = Factura(len(factutas)+1, cliente)
    continuar: bool = True

    while continuar:

        zapatilla: Zapatilla = buscar_zapatilla()
        cantidad: int = int(input("Ingrese la cantidad: "))
        factura.detalle.append(FacturaDetalle(
            zapatilla.codigo, cantidad, zapatilla.precio, zapatilla.talla))
        
        condicion: str = str(input("SI para agregar zapatillas: "))

        if condicion == "SI":
            continuar = True
        else:
            continuar = False
            factura.calcular_igv()
            factutas.append(factura)


def listar_factura():
    for factura in factutas:
        Factura.convertir_a_string(factura)

def buscar_factura():
    numero:int=int(input("Ingrese el numero de la factura: "))
    for factura in factutas:
        if factura.numero==numero:
            Factura.convertir_a_string(factura)
            print("===========================")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)


def main():
    continuar: bool = True

    while continuar:
        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("       1: PARA AGREGAR PERSONA           ")
        print("       2: PARA LISTAR PERSONAS           ")
        print("       3: PARA BUSCAR PERSONA            ")
        print("       4: PARA EDITAR PERSONA            ")
        print("       5: PARA ELIMINAR PERSONA          ")
        print("       6: PARA AGREGAR ZAPATILLA         ")
        print("       7: PARA LISTAR ZAPATILLA          ")
        print("       8: PARA EDITAR ZAPATILLA          ")
        print("       9: PARA ELIMINAR ZAPATILLA        ")
        print("       10: PARA BUSCAR ZAPATILLA         ")
        print("       15: PARA CREAR FACTURA            ")
        print("       16: PARA LISTAR  FACTURA          ")
        print("       17: PARA BUSCAR FACTURA           ")
        print("       18: PARA IMPRIMIR FACTURA         ")
        print("       20: PARA SALIR                    ")
        print ("****************************************")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                zapatilla()
            case "7":
                listar_zapatilla()
            case "8":
                editar_zapatilla()
            case "9":
                eliminar_zapatilla()
            case "10":
                buscar_zapatilla()
            case "15":
                nueva_factura()
            case "16":
                listar_factura()
            case "17":
                buscar_factura()
            case "20":
                continuar = False


if __name__ == '__main__':
    main()
