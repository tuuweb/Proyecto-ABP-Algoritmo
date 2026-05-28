from tipos_juego import JuegoSingleplayer, JuegoMultiplayer, JuegoMobile

# ── Entradas seguras ──────────────────────────────────────────────────────────

def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  El minimo es {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  El maximo es {maximo}.")
                continue
            return valor
        except ValueError:
            print("  Eso no es un numero. Intenta de nuevo.")

def pedir_texto(mensaje):
    while True:
        v = input(mensaje).strip()
        if v:
            return v
        print("  Este campo no puede quedar vacio.")

def pedir_si_no(mensaje):
    while True:
        r = input(mensaje).strip().lower()
        if r in ("s", "n"):
            return r == "s"
        print("  Escribe 's' para si o 'n' para no.")

# ── Agregar segun tipo ────────────────────────────────────────────────────────

def agregar_juego(catalogo):
    print("\n-- Agregar juego --")
    print("  1. Singleplayer")
    print("  2. Multiplayer")
    print("  3. Mobile")
    tipo = input("Tipo de juego (1/2/3): ").strip()

    if tipo not in ("1", "2", "3"):
        print("Tipo invalido.")
        return

    nombre     = pedir_texto("Nombre del juego: ")
    plataforma = pedir_texto("Plataforma (PC, PS5, Xbox, iOS, Android...): ")
    dificultad = pedir_entero("Dificultad (1-10): ", minimo=1, maximo=10)
    horas      = pedir_entero("Horas jugadas: ", minimo=0)

    try:
        if tipo == "1":
            historia   = pedir_texto("Resumen de la historia: ")
            completado = pedir_si_no("Lo completaste? (s/n): ")
            juego = JuegoSingleplayer(nombre, plataforma, dificultad, horas, historia, completado)

        elif tipo == "2":
            print("  Modos: competitivo, cooperativo, battle royale, casual")
            modo    = pedir_texto("Modo de juego: ")
            ranking = pedir_entero("Ranking actual (0 = sin ranking): ", minimo=0)
            juego = JuegoMultiplayer(nombre, plataforma, dificultad, horas, modo, ranking)

        else:
            energia     = pedir_entero("Energia maxima: ", minimo=1)
            micropagos  = pedir_si_no("Tiene micropagos? (s/n): ")
            juego = JuegoMobile(nombre, plataforma, dificultad, horas, energia, micropagos)

        if catalogo.agregar(juego):
            print(f"\nListo! '{juego.nombre}' agregado como {juego.tipo()}.")

    except ValueError as e:
        print(f"Error al crear el juego: {e}")

# ── Ver catalogo ──────────────────────────────────────────────────────────────

def mostrar_catalogo(catalogo):
    juegos = catalogo.listar()
    if not juegos:
        print("\nEl catalogo esta vacio.")
        return
    print(f"\n{catalogo}")
    for j in juegos:
        j.mostrar_info()

# ── Buscar ────────────────────────────────────────────────────────────────────

def buscar_juego(catalogo):
    nombre = pedir_texto("Nombre del juego a buscar: ")
    juego = catalogo.buscar(nombre)
    if juego:
        juego.mostrar_info()
    else:
        print(f"'{nombre}' no esta en el catalogo.")

# ── Actualizar horas ──────────────────────────────────────────────────────────

def sumar_horas(catalogo):
    if len(catalogo) == 0:
        print("\nNo hay juegos en el catalogo.")
        return
    nombre = pedir_texto("Nombre del juego: ")
    juego = catalogo.buscar(nombre)
    if juego:
        horas = pedir_entero("Cuantas horas le sumamos: ", minimo=1)
        juego.actualizar_horas(horas)
    else:
        print(f"'{nombre}' no esta en el catalogo.")

# ── Eliminar ──────────────────────────────────────────────────────────────────

def eliminar_juego(catalogo):
    if len(catalogo) == 0:
        print("\nEl catalogo esta vacio.")
        return
    nombre = pedir_texto("Nombre del juego a eliminar: ")
    juego = catalogo.buscar(nombre)
    if not juego:
        print(f"'{nombre}' no esta en el catalogo.")
        return
    if pedir_si_no(f"Seguro que quieres eliminar '{juego.nombre}'? (s/n): "):
        catalogo.eliminar(nombre)
        print(f"'{juego.nombre}' eliminado.")
    else:
        print("Cancelado.")

# ── Filtros ───────────────────────────────────────────────────────────────────

def filtrar_juegos(catalogo):
    print("\n-- Filtrar por --")
    print("  1. Tipo (Singleplayer / Multiplayer / Mobile)")
    print("  2. Dificultad (Facil / Intermedio / Dificil)")
    opcion = input("Elige (1/2): ").strip()

    if opcion == "1":
        print("  1. Singleplayer  2. Multiplayer  3. Mobile")
        t = input("Tipo: ").strip()
        from tipos_juego import JuegoSingleplayer, JuegoMultiplayer, JuegoMobile
        mapa = {"1": JuegoSingleplayer, "2": JuegoMultiplayer, "3": JuegoMobile}
        if t not in mapa:
            print("Opcion invalida.")
            return
        resultado = catalogo.filtrar_por_tipo(mapa[t])
        nombre_tipo = ["Singleplayer","Multiplayer","Mobile"][int(t)-1]

    elif opcion == "2":
        nivel = pedir_texto("Nivel (Facil / Intermedio / Dificil): ").capitalize()
        if nivel not in ("Facil", "Intermedio", "Dificil"):
            print("Nivel invalido.")
            return
        resultado = catalogo.filtrar_por_dificultad(nivel)
        nombre_tipo = nivel

    else:
        print("Opcion invalida.")
        return

    if not resultado:
        print(f"No hay juegos de tipo/nivel '{nombre_tipo}'.")
    else:
        print(f"\nJuegos encontrados ({len(resultado)}):")
        for j in resultado:
            j.mostrar_info()

# ── Accion especial segun tipo ────────────────────────────────────────────────

def accion_especial(catalogo):
    nombre = pedir_texto("Nombre del juego para accion especial: ")
    juego = catalogo.buscar(nombre)
    if not juego:
        print(f"'{nombre}' no esta en el catalogo.")
        return

    if isinstance(juego, JuegoSingleplayer):
        juego.marcar_completado()

    elif isinstance(juego, JuegoMultiplayer):
        nuevo = pedir_entero("Nuevo ranking: ", minimo=0)
        juego.actualizar_ranking(nuevo)

    elif isinstance(juego, JuegoMobile):
        print("  1. Usar energia  2. Recargar energia")
        op = input("Accion (1/2): ").strip()
        if op == "1":
            cantidad = pedir_entero("Cuanta energia usar: ", minimo=1)
            juego.usar_energia(cantidad)
        elif op == "2":
            juego.recargar_energia()
        else:
            print("Opcion invalida.")

# ── Estadisticas ──────────────────────────────────────────────────────────────

def mostrar_estadisticas(catalogo):
    stats = catalogo.estadisticas()
    if not stats:
        print("\nNo hay juegos suficientes para estadisticas.")
        return
    print("\n=== ESTADISTICAS ===")
    print(f"  Total de juegos   : {stats['total']}")
    print(f"  Horas totales     : {stats['total_horas']}h")
    print(f"  Mas jugado        : {stats['mas_jugado'].nombre} ({stats['mas_jugado'].horas_jugadas}h)")
    print(f"  Mas dificil       : {stats['mas_dificil'].nombre} ({stats['mas_dificil'].dificultad}/10)")
    print(f"  Objetos creados   : {stats['total']} (Videojuego.total_juegos = {catalogo.listar()[0].__class__.total_juegos if stats['total'] else 0})")
