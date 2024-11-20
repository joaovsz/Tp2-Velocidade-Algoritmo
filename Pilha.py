class Pilha:
    def __init__(self, tamanho_maximo=10):
        # Definimos o tamanho máximo da pilha e criamos uma lista vazia para armazenar os itens
        self.tamanho_maximo = tamanho_maximo
        self.itens = [None] * tamanho_maximo  # Lista com tamanho fixo
        self.topo = -1  # Indicador do topo da pilha, começa em -1 (pilha vazia)

    def is_empty(self):
        # Verifica se a pilha está vazia
        return self.topo == -1

    def is_full(self):
        # Verifica se a pilha está cheia
        return self.topo == self.tamanho_maximo - 1

    def push(self, item):
        # Adiciona um item no topo da pilha
        if self.is_full():
            print("Erro: A pilha está cheia")
            return
        self.topo += 1  # Move o topo para o próximo índice
        self.itens[self.topo] = item

    def pop(self):
        # Remove e retorna o item do topo da pilha
        if self.is_empty():
            print("Erro: A pilha está vazia")
            return None
        item = self.itens[self.topo]  # Pega o item do topo
        self.itens[self.topo] = None  # Remove o item do topo
        self.topo -= 1  # Move o topo para o índice anterior
        return item

    def peek(self):
        # Retorna o item do topo sem removê-lo
        if self.is_empty():
            print("Erro: A pilha está vazia")
            return None
        return self.itens[self.topo]

    def size(self):
        # Retorna o número de elementos na pilha
        return self.topo + 1

    def display(self):
        # Exibe o conteúdo da pilha
        if self.is_empty():
            print("A pilha está vazia")
        else:
            print("Pilha:", end=" ")
            for i in range(self.topo + 1):
                print(self.itens[i], end=" ")
            print()

# Exemplo de uso
pilha = Pilha(5)  # Pilha com tamanho máximo de 5
pilha.push(10)
pilha.push(20)
pilha.push(30)
pilha.display()  # Exibe: Pilha: 10 20 30

print("Topo da pilha:", pilha.peek())  # Saída: 30
print("Tamanho da pilha:", pilha.size())  # Saída: 3

pilha.pop()
pilha.display()  # Exibe: Pilha: 10 20
print("Topo da pilha agora:", pilha.peek())  # Saída: 20
