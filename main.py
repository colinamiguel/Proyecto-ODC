from List import *
from Functions import *



prueba = Linked_list()
prueba2 = Linked_list()


#########################################################

prueba.append(1)
prueba.append(2)
prueba.append(3)
prueba.append(4)
prueba.append(5)
prueba.append(6)
prueba.append(7)
prueba.append(8)
prueba.append(9)
prueba.append(10)
prueba.append(11)
prueba.append(12)
prueba.append(13)
prueba.append(14)
prueba.append(15)
prueba.append(16)
prueba.append(17)
prueba.append(18)
prueba.append(19)
prueba.append(20)
prueba.append(21)
prueba.append(54)

prueba.print_list()
print(prueba.Search(54))
print('--------------------------------')

#########################################################

lineas_Facheras = "------------------------------------------------------"
mensaje_Intro = "Bienvenido a la Libreria Publica de Manhattan!\n\nQue desea hacer?\n1. Insertar un nuevo libro\n2. Buscar un libro\n3. Prestar un libro\n4. Devolver un libro\n5. Eliminar libro"

def Inicio():
    print(lineas_Facheras)
    print(mensaje_Intro)
    

def Main():

    Inicio()
    opcion = input('Ingrese el numero de la operacion:' )

    if opcion.isdigit :
        
        if int(opcion) >=1 and int(opcion) <=5:

            Opcion(opcion)
        else:

            Dato_mal_suministrado()
    else:

        Dato_mal_suministrado()

def Opcion(opcion):

    if int(opcion) ==1:

        while True:
            
            print("La cota es un codigo unico que representa cada uno de los libros en la bibloteca\nesta conformado por 6 letras al inicio y 2 digitos")
            cota = input("Ingrese la cota del libro (ejem: MATBYZ01): ")

            if (not cota[0:6].isalpha) and (not cota[6:].isdigit):

                break

        print("El titulo es un nombre unico de libro con un maximo de 30 caracteres")
        titulo = input("Ingrese el titulo del libro (ejem: El Principito): ")

        print("El serial de 12 digitos, es un numero unico de libro puesto por la editorial")
        serial = input("Ingrese el serial del libro (ejem: 000012345678): ")

        disponibles = input("Ingrese el numero de libros disponibles: ")

        prestados = input("Ingrese el numero de libros prestados: ")
    elif int(opcion) ==2:

        print("buscar libro")
    elif int() ==3:

        print("Prestar libro")
    elif int() ==4:

        print("Devolver libro")
    else:

        print("Eliminar libro")

def Dato_mal_suministrado():

    print("El dato que se le ha pedido suministrar es incorrecto, vuelva a intentarlo")
    Main()

Main()