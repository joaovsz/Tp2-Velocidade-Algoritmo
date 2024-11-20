class Fila:
    def __init__(self, capacidade):
        # Inicializa a fila com uma capacidade fixa
        self.capacidade = capacidade
        self.itens = [None] * capacidade  # Cria uma lista com o tamanho máximo
        self.inicio = 0  # Índice do primeiro elemento
        self.fim = 0  # Índice para adicionar o próximo elemento
        self.tamanho = 0  # Número de elementos na fila

    def is_empty(self):
        # Verifica se a fila está vazia
        return self.tamanho == 0

    def is_full(self):
        # Verifica se a fila está cheia
        return self.tamanho == self.capacidade

    def enqueue(self, item):
        # Adiciona um item ao final da fila
        if self.is_full():
            print("Erro: A fila está cheia")
            return
        
        self.itens[self.fim] = item  # Adiciona o item na posição do fim
        self.fim += 1  # Move o índice do fim
        self.tamanho += 1  # Incrementa o tamanho
        
        # Se o índice do fim atingir a capacidade, reinicia para o início (comportamento circular)
        if self.fim == self.capacidade:
            self.fim = 0

    def dequeue(self):
        # Remove e retorna o item do início da fila
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        
        item = self.itens[self.inicio]  # Pega o item do início
        self.itens[self.inicio] = None  # Limpa a posição
        self.inicio += 1  # Move o índice do início
        self.tamanho -= 1  # Decrementa o tamanho
        
        # Se o índice do início atingir a capacidade, reinicia para o início (comportamento circular)
        if self.inicio == self.capacidade:
            self.inicio = 0
            
        return item

    def peek(self):
        # Retorna o item do início da fila sem removê-lo
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens[self.inicio]

    def size(self):
        # Retorna o número de elementos na fila
        return self.tamanho

    def display(self):
        # Exibe os elementos da fila
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", end=" ")
            for i in range(self.tamanho):
                index = (self.inicio + i) % self.capacidade  # Calcula o índice circular
                print(self.itens[index], end=" ")
            print()


# Exemplo de uso
fila = Fila(5)  # Cria uma fila com capacidade de 5
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
fila.display()  # Exibe: Fila: 10 20 30

print("Elemento no início da fila:", fila.peek())  # Saída: 10
print("Tamanho da fila:", fila.size())  # Saída: 3

fila.dequeue()
fila.display()  # Exibe: Fila: 20 30
print("Elemento no início da fila agora:", fila.peek())  # Saída: 20
