# Classe base Cidade
class Cidade:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Esta é a cidade de {self.nome}.")

# Classe derivada Capital
class Capital(Cidade):
    def __init__(self, nome, estado):
        super().__init__(nome)
        self.estado = estado

    def apresentar(self):
        print(f"Esta é a capital {self.nome}, localizada no estado de {self.estado}.")

# Classe derivada Interior
class Interior(Cidade):
    def __init__(self, nome, estado):
        super().__init__(nome)
        self.estado = estado

    def apresentar(self):
        print(f"Este é o interior de {self.nome}, localizado no estado de {self.estado}.")

# Instâncias das classes
brasilia = Capital("Brasília", "Distrito Federal")
catalao = Interior("Catalão", "Goiás")

# Chamada dos métodos apresentar()
brasilia.apresentar()
catalao.apresentar()
