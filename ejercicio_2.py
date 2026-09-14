
# Creamos la lista vacía
alumnos = []
# Se consulta cuántos alumnos se van a registrar.
cantidad = int(input("¿Cuántos alumnos desea registrar?: "))
# En caso de que sean muchos, se repite el proceso de creación
for i in range(cantidad):
    # Mostrar qué alumno se esta registrando.
    print("\nAlumno", i + 1)
    # Pedimos el nombre.
    Nombre = input("Ingrese el nombre: ")
    # Pedimos el apellido.
    Apellido = input("Ingrese el apellido: ")
    # Pedimos el DNI y se convierte a entero.
    DNI = int(input("Ingrese el DNI: "))
    # Pedimos el promedio y se convierte a decimal.
    Promedio = float(input("Ingrese el promedio: "))
    # Creamos un diccionario con los datos.
    alumno = {
        "nombre": Nombre,
        "apellido": Apellido,
        "dni": DNI,
        "promedio": Promedio
    }
    # Agregamos el diccionario a la lista.
    alumnos.append(alumno)
# Mostramos los alumnos registrados.
print("\nLista completa de alumnos registrados e ingresados:")
print(alumnos)