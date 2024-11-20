def contar_pedidos_impares(pilha):
    return sum(1 for pedido in pilha if pedido % 2 != 0)

def contar_pedidos_pares(pilha):
    return sum(1 for pedido in pilha if pedido % 2 == 0)

def inverter_fila(fila):
    return fila[::-1]

def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def contar_livros_impares(fila):
    return sum(1 for livro in fila if livro % 2 != 0)

class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        self.fila.append(nome)

    def atender_cliente(self):
        if self.fila:
            return self.fila.pop(0)
        else:
            return None

    def tamanho_fila(self):
        return len(self.fila)

class TabelaHash:
    def __init__(self, tamanho):
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % len(self.tabela)

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        for i, item in enumerate(self.tabela[indice]):
            if item[0] == chave:
                del self.tabela[indice][i]
                return

pilha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fila = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
lista = [5, 3, 8, 6, 2, 7, 4, 1]

print("Pedidos ímpares:", contar_pedidos_impares(pilha))
print("Pedidos pares:", contar_pedidos_pares(pilha))
print("Fila invertida:", inverter_fila(fila))
print("Lista ordenada:", ordenar_lista(lista))
print("Livros ímpares na fila:", contar_livros_impares(fila))

fila_atendimento = FilaAtendimento()
fila_atendimento.adicionar_cliente("Cliente 1")
fila_atendimento.adicionar_cliente("Cliente 2")
print("Atender cliente:", fila_atendimento.atender_cliente())
print("Tamanho da fila:", fila_atendimento.tamanho_fila())

tabela_hash = TabelaHash(10)
tabela_hash.inserir("chave1", "valor1")
tabela_hash.inserir("chave2", "valor2")
print("Buscar chave1:", tabela_hash.buscar("chave1"))
tabela_hash.remover("chave1")
print("Buscar chave1 após remover:", tabela_hash.buscar("chave1"))
