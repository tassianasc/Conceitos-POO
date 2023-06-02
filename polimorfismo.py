# Classe base Cidade
class Cidade:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        print(f"Bem-vindo(a) à cidade de {self.nome}!")

# Classe derivada Capital
class Capital(Cidade):
    def saudacao(self):
        print(f"Bem-vindo(a) à capital {self.nome}!")

# Classe derivada Interior
class Interior(Cidade):
    def saudacao(self):
        print(f"Bem-vindo(a) ao interior de {self.nome}!")

# Função que recebe uma lista de cidades e chama o método saudacao()
def cumprimentar_cidades(cidades):
    for cidade in cidades:
        cidade.saudacao()

# Instâncias das classes
brasilia = Capital("Brasília")
goiania = Capital("Goiânia")
catalao = Interior("Catalão")
rio_de_janeiro = Capital("Rio de Janeiro")

# Lista de cidades
lista_cidades = [brasilia, goiania, catalao, rio_de_janeiro]

# Chamada da função cumprimentar_cidades()
cumprimentar_cidades(lista_cidades)
