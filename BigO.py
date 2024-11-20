# Função 1
def funcao1(n):
    for i in range(n):
        print(i)

# Função 2
def funcao2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# Função 3
def funcao3(n):
    if n <= 1:
        return n
    return funcao3(n - 1) + funcao3(n - 2)

# funcao1(10)
funcao2(10)