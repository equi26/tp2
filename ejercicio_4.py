
# Creamos una lista vacía
alumnos = []
# Iniciamos un bucle infinito
while True:
    # Pedimos el nombre del alumno. En el caso de que se detecte SALIR, se cancela todo.
    nombre = input(
        "\nIngrese el nombre del alumno "
        "(o escriba SALIR para terminar): "
    )
    # Comprobar si de verdad va a salir.
    if nombre.upper() == "SALIR":
        break
    # Pedimos apellido.
    apellido = input("Ingrese el apellido: ")
    # Pedimos DNI.
    dni = int(input("Ingrese el DNI: "))
    # Creamos una variable para saber si el DNI ya existe.
    dni_repetido = False
    # Recorremos todos los alumnos registrados.
    for alumno in alumnos:
        # Comparar el DNI ingresado con el DNI de cada alumno.
        if alumno["dni"] == dni:
            # Si encontramos el mismo DNI, indicar que está repetido.
            dni_repetido = True
            # Salimos del recorrido porque ya encontramos el DNI.
            break
    # Comprobar si el DNI está repetido.
    if dni_repetido:
        # Rechazar el registro.
        print("\nError: el DNI ya existe.")
        # Informar que no se guarda el alumno.
        print("El alumno no fue registrado.")
    else:
        # Pedimos el promedio solamente si el DNI no está repetido.
        promedio = float(input("Ingrese el promedio: "))
        # Creamos el diccionario del alumno.
        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "promedio": promedio
        }
        # Agregamos el alumno a la lista.
        alumnos.append(alumno)
        # Informar que fue registrado.
        print("\nAlumno registrado correctamente.")
# Cuando el usuario escribe SALIR, mostramos todos los alumnos.
print("\n================================")
print("ALUMNOS REGISTRADOS")
print("================================")
# Mostramos la lista de alumnos.
print(alumnos)
