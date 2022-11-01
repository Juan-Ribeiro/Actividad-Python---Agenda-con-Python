# Autor: Juan Ribeiro
# Año: 2021
from agenda import Agenda

# Demostracion - Menu interactivo
if __name__ == '__main__':
    agenda = Agenda()


    def bienvenida():
        print("Bienvenido/a")


    def menu_principal():
        print()
        print("Seleccione una de las siguientes opciones: ")
        print("1 - Crear un nuevo contacto")
        print("2 - Devolver un contacto por nombre")
        print("3 - Devolver todos los contactos")
        print("4 - Agregar datos a contacto existente")
        print("5 - Eliminar un contacto existente")
        print("6 - Guardar los datos actuales en disco")
        print("7 - Cargar datos desde el disco")
        print("0 - Salir")


    def menu_modificar_contacto():
        print("Seleccione uno de los siguientes campos a agregar o modificar: ")
        print("1 - Telefono")
        print("2 - Email")
        print("3 - Domicilio")
        print("0 - Volver")


    valor_menu, funcionando = 0, True
    bienvenida(), menu_principal()
    # Nota: Introducir solo un valor acorde a las opciones dadas, de lo contrario el programa termina
    # No llegue a encontrar una forma de atrapar la excepcion 'ValueError'
    while funcionando:
        valor_menu = int(input())

        if valor_menu == 1:
            nombre = input("Ingrese el nombre del nuevo contacto: ")
            try:
                agenda.crear_contacto(nombre)
                print("Contacto agregado: " + nombre)
            except ContactoYaExistenteException as ceex:
                print("Ya existe un contacto con este nombre: " + nombre)
            finally:
                menu_principal()

        if valor_menu == 2:
            nombre = input("Ingrese el nombre del contacto: ")
            try:
                print(agenda.devolver_contacto(nombre))
            except ContactoInexistenteException:
                print(ciex)
            finally:
                menu_principal()

        if valor_menu == 3:
            for contacto in agenda.contactos.items():
                print(contacto)
            menu_principal()

        if valor_menu == 4:
            nombre = input("Ingrese el nombre del contacto a modificar: ")
            try:
                contacto = agenda.devolver_contacto(nombre)

                opcion_contacto = 0
                modificando = True
                while modificando:
                    menu_modificar_contacto()
                    opcion_contacto = int(input())
                    if opcion_contacto == 1:
                        print("Ingrese el tipo de telefono: ")
                        tipo = input()
                        print("Ingrese el numero de telefono: ")
                        numero = input()
                        contacto.agregar_telefono(tipo, numero)
                    if opcion_contacto == 2:
                        print("Ingrese el nuevo email: ")
                        email = input()
                        contacto.email = email
                    if opcion_contacto == 3:
                        print("Ingrese el tipo de dato de domicilio: ")
                        tipo_dato = input()
                        print("Ingrese el valor del dato de domicilio: ")
                        valor_dato = input()
                        contacto.agregar_dato_domicilio(tipo_dato, valor_dato)
                    if opcion_contacto == 0:
                        modificando = False

            except ContactoInexistenteException as ciex:
                print(ciex)
            finally:
                menu_principal()

        if valor_menu == 5:
            print("Ingrese el nombre del contacto a eliminar: ")
            nombre = input()
            try:
                agenda.eliminar_contacto(nombre)
                print("Contacto eliminado: " + nombre)
            except ContactoInexistenteException as ciex:
                print(ciex)
            finally:
                menu_principal()

        if valor_menu == 6:
            print("Ingrese el nombre del archivo a guardar: ")
            nombre_archivo = input()
            agenda.guardar_datos_en_disco(nombre_archivo)
            menu_principal()

        if valor_menu == 7:
            print("Ingrese el nombre del archivo a cargar: ")
            nombre_archivo = input()
            agenda.cargar_desde_disco(nombre_archivo)
            menu_principal()

        if valor_menu == 0:
            funcionando = False
