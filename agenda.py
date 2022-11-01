# Autor: Juan Ribeiro
# Año: 2021

import shelve


class Agenda(object):
    def __init__(self, contactos={}):
        """
        Crea una agenda vacia para almacenar objetos de tipo Contacto
        """
        self.contactos = contactos

    def crear_contacto(self, nombre_contacto):
        """
        :param nombre_contacto: tipo string, autodescriptivo
        Crea un nuevo Contacto a partir del nombre dado, si este ya existe se lanza una excepcion
        """
        if nombre_contacto not in self.contactos:
            self.contactos[nombre_contacto] = Contacto(nombre_contacto)
        else:
            raise ContactoYaExistenteException

    def devolver_contacto(self, nombre_contacto):
        """
        :param nombre_contacto: tipo string, autodescriptivo
        :return: el contacto con el nombre especificado
        """
        if nombre_contacto in self.contactos:
            return self.contactos[nombre_contacto]

    def eliminar_contacto(self, nombre_contacto):
        """
        :param nombre_contacto: tipo string, autodescriptivo
        Elimina el contacto con el nombre especificado, si este no existe en la agenda lanza una excepcion
        """
        if nombre_contacto in self.contactos:
            del self.contactos[nombre_contacto]
        else:
            raise ContactoInexistenteException

    def guardar_datos_en_disco(self, nombre_archivo):
        """
        :param nombre_archivo: tipo string, autodescriptivo
        Se almacenan los datos de los contactos en un archivo indexado con nombre especificado por medio de 'shelve'
        """
        with shelve.open(nombre_archivo, "c") as db:
            for clave_nombre, valor_contacto in self.contactos.items():
                db[clave_nombre] = valor_contacto

    def cargar_desde_disco(self, nombre_archivo):
        """
        :param nombre_archivo: tipo string, autodescriptivo
        Carga en la agenda los datos de Contactos creados a partir de un archivo indexado por 'shelve'
        """
        with shelve.open(nombre_archivo) as db:
            for clave, valor in db.items():
                self.contactos[clave] = valor


class Contacto(object):
    def __init__(self, nombre, tel={}, email="", domicilio={}):
        """
        :type: string
        :param nombre: nombre del contacto, tambien la clave en el diccionario de la Agenda
        :param tel: tipo dict con objetos "'tipo_telefono' : 'numero_telefono'" Ej: {"Casa":11-2233-4455}
        :param email: tipo string, unico
        :param domicilio: tipo dict con objetos "'tipo_dato' : 'valor_dato'". Ej: {"Calle":"Las Petunias", "Num":6544}
        """
        self.nombre = nombre
        self.tel = tel
        self.email = email
        self.domicilio = domicilio

    def agregar_telefono(self, tipo_telefono, numero_telefono):
        """
        :param tipo_telefono: tipo string, autodescriptivo
        :param numero_telefono: tipo int, autodescriptivo
        :return:
        """
        self.tel[tipo_telefono] = numero_telefono

    def agregar_dato_domicilio(self, tipo_dato, valor_dato):
        """
        :param tipo_dato: tipo string, indica el tipo de dato acerca del domicilio. Ej: "Direccion"
        :param valor_dato: tipo string, indica el valor del dato acerca del domicilio. Ej: "El Pensamiento 1234"
        :return:
        """
        self.domicilio[tipo_dato] = valor_dato

    def __repr__(self):
        """
        :return: el conjunto de atributos del contacto en forma de stirng
        """
        return str(self.__dict__)


# Excepciones
class ContactoYaExistenteException(Exception):
    pass


class ContactoInexistenteException(Exception):
    pass