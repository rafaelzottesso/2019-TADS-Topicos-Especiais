# Criar uma lista vazia
lista = []
# Criar uma lista com tamanho 10
lista2 = [""]*10

# Adicionar um elemento na lista
lista.append(5)
lista.append(18)
lista.append(1)
lista.append(3)
lista.append(11)
lista.append(15)
lista.append(4)

# Alterar um valor da lista
lista[3] = 44

print("Resultado da lista:", lista)

# Calcular tamanho da lista
t = len(lista)
i = 0

while i < t:

    # print("Na posição", i, "tem o valor", lista[i])
    print("Na posição {} tem o valor {}.".format(i, lista[i]))
    i += 1

print("\n===============================\n")

# Usando o for da maneira foreach
for x in lista:
    print("Valor da lista:", x)


# Uso do for normal
# len calcula o tamanho da lista e range cria uma sequência numérica de 0 até o tamanho da lista
for i in range( len(lista) ):
    print("Na posição {} tem o valor {}.".format(i, lista[i]))

# Criação de funções
def dobro(num):
    d = num * 2
    print("O dobro de {} é {}.".format(num, d) )
    return d, num

a, b = dobro(5)
print("Os retornos são: {} e {}.".format(a, b) )
