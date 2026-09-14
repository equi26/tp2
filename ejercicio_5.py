
# Creamos una función
def registrar_nuevo_alumno():
    # Pedimos nombre y apellido.
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    # convertir DNI a número entero.
    try:
        # Pedimos DNI.
        dni = int(input("Ingresar DNI: "))
    # Si el usuario escribe letras, tirar error ValueError.
    except ValueError:
        print("Error: el DNI debe ser un número.")
        # Función acabada.
        return
    # Convertir la edad a número entero.
    try:
        # Pedimos edad.
        edad = int(input("Ingresar edad: "))
    # De nuevo ValueError si pone letras.
    except ValueError:
        print("Error: la edad debe ser un número.")
        return
    # Promedio.
    promedio = float(input("Ingresar promedio: "))
    # Creamos el diccionario.
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad,
        "promedio": promedio
    }
    # Abrir o crear archivo registros.txt utilizando el modo "a".
    with open("registros.txt", "a", encoding="utf-8") as archivo:
        # Escribir datos del alumno en una sola línea.
        archivo.write(
            f"Nombre: {nombre} | "
            f"Apellido: {apellido} | "
            f"DNI: {dni} | "
            f"Edad: {edad} | "
            f"Promedio: {promedio}\n"
        )
    # Informar que el alumno fue registrado.
    print("\nAlumno registrado correctamente.")
    # Mostrar datos creados.
    print("Datos del alumno actualizados:")
    print(alumno)
# Llamar a la función para registrar un nuevo alumno.
registrar_nuevo_alumno()