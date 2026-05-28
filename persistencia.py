import json
import os
from tipos_juego import JuegoSingleplayer, JuegoMultiplayer, JuegoMobile

ARCHIVO = "catalogo.json"

def guardar(catalogo):
    datos = []
    for j in catalogo.listar():
        base = {
            "tipo":          j.tipo(),
            "nombre":        j.nombre,
            "plataforma":    j.plataforma,
            "dificultad":    j.dificultad,
            "horas_jugadas": j.horas_jugadas,
        }
        if isinstance(j, JuegoSingleplayer):
            base["historia"]   = j.historia
            base["completado"] = j.completado
        elif isinstance(j, JuegoMultiplayer):
            base["modo"]    = j.modo
            base["ranking"] = j.ranking
        elif isinstance(j, JuegoMobile):
            base["energia_max"]   = j.energia_max
            base["tiene_compras"] = j.tiene_compras

        datos.append(base)

    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump({"usuario": catalogo.nombre_usuario, "juegos": datos}, f, ensure_ascii=False, indent=2)

def cargar(catalogo):
    if not os.path.exists(ARCHIVO):
        return  # primera vez, no hay nada guardado

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        datos = json.load(f)

    for j in datos.get("juegos", []):
        try:
            tipo = j["tipo"]
            if tipo == "Singleplayer":
                obj = JuegoSingleplayer(j["nombre"], j["plataforma"], j["dificultad"],
                                        j["horas_jugadas"], j["historia"], j["completado"])
            elif tipo == "Multiplayer":
                obj = JuegoMultiplayer(j["nombre"], j["plataforma"], j["dificultad"],
                                       j["horas_jugadas"], j["modo"], j["ranking"])
            elif tipo == "Mobile":
                obj = JuegoMobile(j["nombre"], j["plataforma"], j["dificultad"],
                                  j["horas_jugadas"], j["energia_max"], j["tiene_compras"])
            else:
                continue
            catalogo.agregar(obj)
        except (ValueError, KeyError):
            pass  # si un registro está corrupto, lo salta sin romper todo
