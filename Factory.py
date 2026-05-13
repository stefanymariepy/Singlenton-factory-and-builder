# ============================================================
# PATRON DE DISEÑO: FACTORY
# Objetivo: centralizar la creacion de objetos en una
# "fabrica". El cliente no necesita saber que subclase
# se crea, solo pide el tipo que necesita.
# ============================================================

# Clase base (interfaz) — define el metodo que todas
# las subclases DEBEN implementar.
class Transporte:
    def entregar(self):
        pass  # metodo abstracto, cada subclase lo sobreescribe

# Subclase 1: implementacion concreta para camion
class Camion(Transporte):
    def entregar(self):
        return "Entrega por carretera en camion"

# Subclase 2: implementacion concreta para barco
class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar en barco"

# Subclase 3: implementacion concreta para avion
class Avion(Transporte):
    def entregar(self):
        return "Entrega por aire en avion"

# LA FABRICA: recibe un string y devuelve el objeto correcto.
# @staticmethod: no necesita instancia de TransporteFactory
# para ser llamado — se usa directo como TransporteFactory.get_transporte()
class TransporteFactory:
    @staticmethod
    def get_transporte(tipo):
        if tipo == "camion":
            return Camion()   # crea y devuelve un Camion
        elif tipo == "barco":
            return Barco()    # crea y devuelve un Barco
        elif tipo == "avion":
            return Avion()    # crea y devuelve un Avion
        else:
            # tipo no reconocido: informa el error y devuelve None
            print(f"  Error: el tipo '{tipo}' no existe.")
            return None

# ---- USO ----
for tipo in ["camion", "barco", "avion"]:
    transporte = TransporteFactory.get_transporte(tipo)
    print(f"Tipo pedido : {tipo}")
    print(f"Resultado   : {transporte.entregar()}")

# tipo incorrecto — activa el manejo de error
TransporteFactory.get_transporte("helicoptero")
