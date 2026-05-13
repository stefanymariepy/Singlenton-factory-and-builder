# ============================================================
# PATRON DE DISEÑO: BUILDER
# Objetivo: construir un objeto complejo (ComboFastFood)
# paso a paso, de forma clara y flexible.
# Cada metodo agrega una parte y retorna 'self' para
# poder encadenar llamadas en una sola expresion.
# ============================================================

# Clase producto: el objeto final que se va a construir.
# Todos los atributos empiezan en None (sin definir).
class ComboFastFood:
    def __init__(self):
        self.hamburguesa = None  # obligatorio
        self.bebida      = None  # obligatorio
        self.papas       = None  # obligatorio
        self.postre      = None  # opcional

    def mostrar(self):
        print("====== TU COMBO ======")
        print(f"  Hamburguesa : {self.hamburguesa}")
        print(f"  Bebida      : {self.bebida}")
        print(f"  Papas       : {self.papas}")
        if self.postre:          # solo muestra postre si fue agregado
            print(f"  Postre      : {self.postre}")
        print("======================")

# Clase Builder: construye ComboFastFood parte por parte.
# Cada metodo asigna un atributo y retorna 'self'
# para permitir el encadenamiento de metodos.
class ComboBuilder:
    def __init__(self):
        self.combo = ComboFastFood()  # crea el objeto vacio

    def agregar_hamburguesa(self, tipo):
        self.combo.hamburguesa = tipo
        return self  # retorna self para encadenar el siguiente metodo

    def agregar_bebida(self, bebida):
        self.combo.bebida = bebida
        return self

    def agregar_papas(self, papas):
        self.combo.papas = papas
        return self

    def agregar_postre(self, postre):
        self.combo.postre = postre
        return self  # opcional, se puede omitir

    def build(self):
        # Validacion: los 3 campos obligatorios deben estar presentes
        if not self.combo.hamburguesa:
            print("  Error: falta la hamburguesa!")
            return None
        if not self.combo.bebida:
            print("  Error: falta la bebida!")
            return None
        if not self.combo.papas:
            print("  Error: faltan las papas!")
            return None
        return self.combo  # entrega el objeto ComboFastFood terminado

# ---- USO: encadenamiento de metodos ----
combo = (ComboBuilder()
         .agregar_hamburguesa("Hamburguesa con queso")
         .agregar_bebida("Coca-Cola grande")
         .agregar_papas("Papas fritas medianas")
         .agregar_postre("Helado de vainilla")  # opcional
         .build())
combo.mostrar()
