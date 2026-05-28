from catalogo import Catalogo
import funciones_catalogo as fc
import persistencia

def mostrar_menu():
    print("\n" + "=" * 42)
    print("       CATALOGO DE VIDEOJUEGOS")
    print("=" * 42)
    print("  1. Agregar juego")
    print("  2. Ver catalogo completo")
    print("  3. Buscar juego")
    print("  4. Actualizar horas de juego")
    print("  5. Accion especial del juego")
    print("  6. Filtrar juegos")
    print("  7. Eliminar juego")
    print("  8. Estadisticas")
    print("  9. Salir")
    print("=" * 42)

def ejecutar_menu():
    nombre = input("Como te llamas? ").strip() or "Jugador"
    mi_catalogo = Catalogo(nombre)

    # carga el catalogo guardado si existe
    persistencia.cargar(mi_catalogo)

    if len(mi_catalogo) > 0:
        print(f"\nBienvenido de vuelta, {nombre}! Se cargaron {len(mi_catalogo)} juego(s) de tu catalogo.")
    else:
        print(f"\nBienvenido, {nombre}! Tu catalogo esta listo.")

    # acciones que modifican el catalogo guardan automaticamente
    def agregar():
        fc.agregar_juego(mi_catalogo)
        persistencia.guardar(mi_catalogo)

    def actualizar():
        fc.sumar_horas(mi_catalogo)
        persistencia.guardar(mi_catalogo)

    def especial():
        fc.accion_especial(mi_catalogo)
        persistencia.guardar(mi_catalogo)

    def eliminar():
        fc.eliminar_juego(mi_catalogo)
        persistencia.guardar(mi_catalogo)

    acciones = {
        "1": agregar,
        "2": lambda: fc.mostrar_catalogo(mi_catalogo),
        "3": lambda: fc.buscar_juego(mi_catalogo),
        "4": actualizar,
        "5": especial,
        "6": lambda: fc.filtrar_juegos(mi_catalogo),
        "7": eliminar,
        "8": lambda: fc.mostrar_estadisticas(mi_catalogo),
    }

    while True:
        mostrar_menu()
        opcion = input("Que quieres hacer? (1-9): ").strip()

        if opcion == "9":
            print(f"\nHasta luego, {nombre}!")
            break
        elif opcion in acciones:
            acciones[opcion]()
        else:
            print("Opcion invalida. Elige un numero del 1 al 9.")

if __name__ == "__main__":
    ejecutar_menu()
