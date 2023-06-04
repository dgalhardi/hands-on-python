from datetime import datetime


# Python Object-Oriented Programming

# Classes
# Utilizadas para criar objetos (instances)
# Objetos sao partes dentro de uma Class (instancias)
# Classes sao utilizadas para agrupar dados e funcoes, podendo reutilizar

class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Joao', 'Lira', 2003)
usuario3 = Funcionarios('Pedro', 'Augusto', 2007)

print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))
