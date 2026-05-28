from videojuego import Videojuego

class JuegoSingleplayer(Videojuego):
    """Juego de un solo jugador. Agrega historia y si fue completado."""

    def __init__(self, nombre, plataforma, dificultad, horas_jugadas, historia, completado=False):
        super().__init__(nombre, plataforma, dificultad, horas_jugadas)
        self.historia   = historia      # descripcion breve de la trama
        self.completado = completado    # True/False

    def tipo(self):
        return "Singleplayer"

    def marcar_completado(self):
        self.completado = True
        print(f"Felicitaciones! Marcaste '{self.nombre}' como completado.")

    def mostrar_info(self):
        super().mostrar_info()
        estado = "Completado" if self.completado else "En progreso"
        print(f"  Historia   : {self.historia}")
        print(f"  Estado     : {estado}")


class JuegoMultiplayer(Videojuego):
    """Juego en linea con otros jugadores. Agrega modo de juego y ranking."""

    MODOS_VALIDOS = ["competitivo", "cooperativo", "battle royale", "casual"]

    def __init__(self, nombre, plataforma, dificultad, horas_jugadas, modo, ranking=0):
        super().__init__(nombre, plataforma, dificultad, horas_jugadas)
        modo_lower = modo.strip().lower()
        if modo_lower not in self.MODOS_VALIDOS:
            raise ValueError(f"Modo invalido. Elige entre: {', '.join(self.MODOS_VALIDOS)}")
        self.modo    = modo_lower
        self.ranking = ranking   # posicion en ranking, 0 = sin ranking

    def tipo(self):
        return "Multiplayer"

    def actualizar_ranking(self, nuevo_ranking):
        if nuevo_ranking < 0:
            print("El ranking no puede ser negativo.")
            return
        self.ranking = nuevo_ranking
        print(f"Ranking de '{self.nombre}' actualizado a #{nuevo_ranking}.")

    def mostrar_info(self):
        super().mostrar_info()
        ranking_txt = f"#{self.ranking}" if self.ranking > 0 else "Sin ranking"
        print(f"  Modo       : {self.modo.capitalize()}")
        print(f"  Ranking    : {ranking_txt}")


class JuegoMobile(Videojuego):
    """Juego para dispositivos moviles. Agrega sistema de energia y compras."""

    def __init__(self, nombre, plataforma, dificultad, horas_jugadas, energia_max, tiene_compras):
        super().__init__(nombre, plataforma, dificultad, horas_jugadas)
        if energia_max <= 0:
            raise ValueError("La energia maxima debe ser mayor a 0.")
        self.energia_max    = energia_max
        self.energia_actual = energia_max
        self.tiene_compras  = tiene_compras   # True si tiene micropagos

    def tipo(self):
        return "Mobile"

    def usar_energia(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        if cantidad > self.energia_actual:
            print(f"No tienes suficiente energia. Solo te quedan {self.energia_actual}.")
            return
        self.energia_actual -= cantidad
        print(f"Usaste {cantidad} de energia en '{self.nombre}'. Te quedan {self.energia_actual}/{self.energia_max}.")

    def recargar_energia(self):
        self.energia_actual = self.energia_max
        print(f"Energia de '{self.nombre}' recargada al maximo ({self.energia_max}).")

    def mostrar_info(self):
        super().mostrar_info()
        compras = "Si" if self.tiene_compras else "No"
        print(f"  Energia    : {self.energia_actual}/{self.energia_max}")
        print(f"  Micropagos : {compras}")
