
#Pedimos nombre del alumno.
Nombre = input("Ingrese el nombre del alumno: ")
# Pedimos apellido del alumno.
Apellido = input("Ingrese el apellido del alumno: ")
# Pedimos DNI y se convierte en número entero.
DNI = int(input("Ingrese el DNI del alumno: "))
# Pedimos promedio y lo convertimos a número decimal.
Promedio = float(input("Ingrese el promedio del alumno: "))
# Creamos un diccionario con los datos del alumno.
alumno = {
    "Nombre": Nombre,
    "Apellido": Apellido,
    "DNI": DNI,
    "Promedio": Promedio
}
# Mostramos datos del alumno.
print("\nDatos de alumnos actualizados e ingresados:")
print(alumno)