from videojuego import Videojuego

class Catalogo:
    """Clase que gestiona la coleccion completa de videojuegos."""

    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self._juegos = []   # lista interna protegida

    def agregar(self, juego):
        if not isinstance(juego, Videojuego):
            raise TypeError("Solo se pueden agregar objetos de tipo Videojuego.")
        for j in self._juegos:
            if j.nombre.lower() == juego.nombre.lower():
                print(f"'{juego.nombre}' ya esta en el catalogo.")
                return False
        self._juegos.append(juego)
        return True

    def buscar(self, nombre):
        for j in self._juegos:
            if j.nombre.lower() == nombre.strip().lower():
                return j
        return None

    def eliminar(self, nombre):
        juego = self.buscar(nombre)
        if juego:
            self._juegos.remove(juego)
            return True
        return False

    def listar(self):
        return list(self._juegos)  # devuelve copia para no exponer la lista interna

    def filtrar_por_tipo(self, tipo_clase):
        # filtra por clase (JuegoSingleplayer, JuegoMultiplayer, etc.)
        return [j for j in self._juegos if isinstance(j, tipo_clase)]

    def filtrar_por_dificultad(self, nivel):
        # nivel: "Facil", "Intermedio" o "Dificil"
        return [j for j in self._juegos if j.evaluar_dificultad() == nivel]

    def estadisticas(self):
        if not self._juegos:
            return None
        total_horas  = sum(j.horas_jugadas for j in self._juegos)
        mas_jugado   = max(self._juegos, key=lambda j: j.horas_jugadas)
        mas_dificil  = max(self._juegos, key=lambda j: j.dificultad)
        return {
            "total":        len(self._juegos),
            "total_horas":  total_horas,
            "mas_jugado":   mas_jugado,
            "mas_dificil":  mas_dificil,
        }

    def __len__(self):
        return len(self._juegos)

    def __str__(self):
        return f"Catalogo de {self.nombre_usuario} — {len(self._juegos)} juego(s)"
