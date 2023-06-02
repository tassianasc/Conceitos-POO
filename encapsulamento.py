class Cidade:
    def __init__(self, nome, estado):
        self.__nome = nome
        self.__estado = estado

    @property
    def nome(self):
        return self.__nome

    @property
    def estado(self):
        return self.__estado

    def apresentar(self):
        print(f"Esta é a cidade de {self.nome}, localizada no estado de {self.estado}.")

# Instância da classe
goiania = Cidade("Goiânia", "Goiás")

# Acessando os atributos encapsulados por meio dos métodos getters
print(goiania.nome)
print(goiania.estado)

# Chamada do método apresentar()
goiania.apresentar()
