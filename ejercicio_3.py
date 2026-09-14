
# Creamos la lista vacía
alumnos = []
# Pedimos nombre del alumno.
nombre = input("Ingrese el nombre del alumno: ")
# Pedimos apellido del alumno.
apellido = input("Ingrese el apellido del alumno: ")
# Pedimos DNI.
dni = int(input("Ingrese el DNI del alumno: "))
# Pedimos la edad y se convierte a entero.
edad = int(input("Ingrese la edad del alumno: "))
# Comprobar si la edad está entre 17 y 99.
if edad >= 17 and edad <= 99:
    # Si la edad es válida, pedimos el promedio.
    promedio = float(input("Ingrese el promedio del alumno: "))
    # Creamos el diccionario del alumno.
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad,
        "promedio": promedio
    }
    # Guardamos el alumno en la lista.
    alumnos.append(alumno)
    print("\nAlumno registrado correctamente.")
    # Mostrar los datos del alumno.
    print(alumno)
else:
    # Si la edad no es válida, mostramos un mensaje.
    print("\nError de validación: El sistema tuvo un error durante el registro.")
    # Informamos que el registro no se guarda por la edad.
    print("Causante: La edad debe estar entre 17 y 99 años.")
    # Mostrar que el registro fue descartado.
    print("El registro fue descartado.")
