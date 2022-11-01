# Agenda con Python
Programa realizado como parte de las actividades semanales de la cátedra 2021 de la materia Estructura de Datos, de la carrera Ingeniería en Computación de la Universidad Nacional de Tres de Febrero.

## Consigna
Escribir un programa para almacenar una agenda telefónica (escribir y leer registros en archivos binarios).

Cada registro de la agenda debe cumplir con el siguiente formato:
```json
rec = {
    "nombre": "Juan",
    "tel": {
        "cel": "15-8888-7777",
        "casa": "4123-5879"
    },
    "email": "juan@umail.com",
    "domicilio": {
        "calle": "Urquiza",
        "nro": 657,
        "piso": 6,
        "depto": "A",
        "localidad": "Caseros"
    }
}

```


Los campos de los diccionarios pueden ser variables, por ejemplo puede tener cualquier cantidad de teléfonos registrados o el domicilio puede no contener información de piso y dpto.

El programa debe proveer mecanismos para:

* Crear un contacto.
* Devolver un contacto por nombre
* Agregar datos a un contacto existente
* Guardar los datos a disco
* Cargar los datos desde el disco

Para la persistencia en disco se requiere usar shelve
