class Videojuego:
    """Clase base. Todo videojuego del catalogo hereda de esta."""
    total_juegos = 0  # atributo de clase: cuenta todos los objetos creados

    def __init__(self, nombre, plataforma, dificultad, horas_jugadas):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")
        if not (1 <= dificultad <= 10):
            raise ValueError("La dificultad debe ser un numero entre 1 y 10.")
        if horas_jugadas < 0:
            raise ValueError("Las horas no pueden ser negativas.")

        self.nombre         = nombre.strip().title()
        self.plataforma     = plataforma.strip()
        self._dificultad    = dificultad   # protegido: se accede via @property
        self.horas_jugadas  = horas_jugadas
        Videojuego.total_juegos += 1

    @property
    def dificultad(self):
        return self._dificultad

    def evaluar_dificultad(self):
        if self._dificultad >= 8:
            return "Dificil"
        elif self._dificultad >= 5:
            return "Intermedio"
        return "Facil"

    def actualizar_horas(self, nuevas_horas):
        if nuevas_horas <= 0:
            print("Las horas a agregar deben ser positivas.")
            return
        self.horas_jugadas += nuevas_horas
        print(f"Listo! Ahora tienes {self.horas_jugadas}h en {self.nombre}.")

    def tipo(self):
        # cada subclase sobreescribe esto (polimorfismo)
        return "General"

    def mostrar_info(self):
        print(f"\n{'='*38}")
        print(f"  {self.nombre}  [{self.tipo()}]")
        print(f"{'='*38}")
        print(f"  Plataforma : {self.plataforma}")
        print(f"  Dificultad : {self.evaluar_dificultad()} ({self._dificultad}/10)")
        print(f"  Horas      : {self.horas_jugadas}h jugadas")

    def __str__(self):
        return f"{self.nombre} | {self.plataforma} | {self.evaluar_dificultad()} | {self.horas_jugadas}h"
