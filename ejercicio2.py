import csv

def main():

# Dar la bienvenida al usuario
    print("Bienvenido al programa de registro de datos.")

    # 1. Pedir al usuario que ingrese los datos
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    Hoobies = input("Ingrese sus hobbies: ")
    comida_favorita = input("Ingrese su comida favorita: ")
    musica_favorita = input("Ingrese su música favorita: ")
    peliculas_favoritas = input("Ingrese sus películas favoritas: ")
    metas_personales = input("Ingrese sus metas personales: ")

    # Guardar los datos en un archivo CSV
    with open('datos.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, edad])

# 2. Leer los datos del archivo CSV y mostrarlos en pantalla
    with open('datos.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        print("\nDatos guardados:")
        for fila in lector:
            print(f"Nombre: {fila[0]}, Edad: {fila[1]}")

# Mostrar un mensaje de despedida
    print("\nGracias por usar el programa. ¡Hasta luego!")

if __name__ == "__main__":
    main()
