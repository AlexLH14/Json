import json
from datetime import date
from datetime import datetime
ARCHIVO_JSON = 'inventario_libros.json'


def cargar_inventario():
    try:
        with open(ARCHIVO_JSON, 'r') as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = {"libros": []}
    return inventario

def guardar_inventario(inventario):
    with open(ARCHIVO_JSON, 'w') as archivo:
        json.dump(inventario, archivo, indent=6)

def anadir_libro(inventario):
    titulo = input("Título: ")
    autor = input("Autor: ")
    año = input("Año de publicación: ")
    isbn = input("ISBN: ")
    editorial = input("Editorial: ")
    disponibilidad_str = input("Disponibilidad (si/no): ").strip().lower()
    disponibilidad = disponibilidad_str == "si"

    # Solicitar la fecha de última actualización al usuario
    fecha_str = input("Fecha de última actualización (formato: DD-MM-YYYY): ")
    fecha_actualizacion = datetime.strptime(fecha_str, "%d-%m-%Y").strftime("%d-%m-%Y")

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "isbn": isbn,
        "informacion": {
            "editorial": editorial,
            "ultima_actualizacion": fecha_actualizacion,
            "disponibilidad": disponibilidad
        }
    }
    inventario["libros"].append(nuevo_libro)
    guardar_inventario(inventario)
    print("Libro añadido con éxito.")
    

def mostrar_libros(inventario):
    if not inventario["libros"]:
        print("No hay libros en el inventario.")
    else:
        for libro in inventario["libros"]:
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['año']}")
            print(f"ISBN: {libro['isbn']}")
            print(f"Editorial: {libro['informacion']['editorial']}")
            print(f"Última Actualización: {libro['informacion']['ultima_actualizacion']}")
            print(f"Disponibilidad: {'Disponible' if libro['informacion']['disponibilidad'] else 'No Disponible'}")
            print("-" * 50)



def actualizar_libro(inventario):
    titulo = input("Título del libro a actualizar: ")
    for libro in inventario["libros"]:
        if libro["titulo"] == titulo:
            libro["autor"] = input("Nuevo autor: ")
            libro["año"] = input("Nuevo año de publicación: ")
            libro["isbn"] = input("Nuevo ISBN: ")
            guardar_inventario(inventario)
            print("Libro actualizado con éxito.")
            return
    print("Libro no encontrado.")



def actualizar_informacion(inventario):
    titulo = input("Título del libro a actualizar: ")
    for libro in inventario["libros"]:
        if libro["titulo"] == titulo:
            libro["autor"] = input("Nuevo autor: ")
            libro["año"] = input("Nuevo año de publicación: ")
            libro["isbn"] = input("Nuevo ISBN: ")
            libro["informacion"]["editorial"] = input("Nueva Editorial: ")
            #libro["informacion"]["ultima_actualizacion"] = datetime(input("fecha de ultima actualizacion: "))
            fecha_str = input("Fecha de última actualización (formato: DD-MM-YYYY): ")
            # Convertir la cadena de entrada a un objeto datetime y luego a date
            fecha_actualizacion = datetime.strptime(fecha_str, "%d-%m-%Y").date()
            libro["informacion"]["ultima_actualizacion"] = fecha_actualizacion.strftime("%d-%m-%Y")
            disponibilidad_str = input("Disponibilidad (si/no): ").strip().lower()
            libro["informacion"]["disponibilidad"] = disponibilidad_str == "si"
            guardar_inventario(inventario)
            print("Libro actualizado con éxito.")
            return
    print("Libro no encontrado.")






def eliminar_libro(inventario):
    titulo = input("Título del libro a eliminar: ")
    for libro in inventario["libros"]:
        if libro["titulo"] == titulo:
            inventario["libros"].remove(libro)
            guardar_inventario(inventario)
            print("Libro eliminado con éxito.")
            return
    print("Libro no encontrado.")

def menu():
    inventario = cargar_inventario()
    while True:
        print("\n--- Gestión de Inventario de Libros ---\n")
        print("1. Añadir libro")
        print("2. Mostrar libros")
        print("3. Actualizar libro")
        print("4. Actualizar info")
        print("5. Eliminar libro")
        print("6. Salir")
        opcion = input("Elige una opción:\n ")
        if opcion == "1":
            anadir_libro(inventario)
        elif opcion == "2":
            mostrar_libros(inventario)
        elif opcion == "3":
            actualizar_libro(inventario)
        elif opcion == "4":
            actualizar_informacion(inventario)
        elif opcion == "5":
            eliminar_libro(inventario)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

if __name__ == "__main__":
    menu()
