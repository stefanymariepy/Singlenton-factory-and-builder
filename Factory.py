# ── Factory en Python ─────────────────────────
class Transporte:
    def entregar(self):
        pass                   # método base (interfaz)

class Camion(Transporte):
    def entregar(self):
        return "Entrega por carretera"

class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar"

class Avion(Transporte):       # puedes agregar más tipos fácilmente
    def entregar(self):
        return "Entrega por aire"

class Factory:
    @staticmethod
    def get_transporte(tipo):
        if   tipo == "camion": return Camion()
        elif tipo == "barco":  return Barco()
        elif tipo == "avion":  return Avion()
        else: raise ValueError(f"Tipo '{tipo}' no reconocido")

# ── Uso ───────────────────────────────────────
t = Factory.get_transporte("barco")
print(t.entregar())   # Entrega por mar