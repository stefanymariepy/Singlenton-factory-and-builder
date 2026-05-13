# ── Builder en Python ─────────────────────────
class Computadora:
    def __init__(self):
        self.cpu = None    # procesador
        self.ram = None    # memoria RAM
        self.gpu = None    # tarjeta gráfica

class Builder:
    def __init__(self):
        self.computadora = Computadora()   # objeto a construir

    def add_cpu(self, cpu):
        self.computadora.cpu = cpu
        return self        # retorna self → permite encadenar

    def add_ram(self, ram):
        self.computadora.ram = ram
        return self

    def add_gpu(self, gpu):
        self.computadora.gpu = gpu
        return self

    def build(self):
        return self.computadora    # entrega el objeto terminado

# ── Uso (encadenado) ──────────────────────────
pc = (Builder()
      .add_cpu("Intel i9")
      .add_ram("32GB")
      .add_gpu("RTX 4090")
      .build())

print(vars(pc))
# {'cpu': 'Intel i9', 'ram': '32GB', 'gpu': 'RTX 4090'}