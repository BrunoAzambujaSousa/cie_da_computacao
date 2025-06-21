import statistics

x = 1
x = 2
print(x)

comprimento = [3, 5, 6, 8, 7, 3]
print(comprimento)
print(sum(comprimento) / len(comprimento)) #soma e média

print(statistics.mean(comprimento))
print(statistics.mode(comprimento))

minimo = min(comprimento)
maximo = max(comprimento)
mediana = statistics.median(comprimento)

print(minimo)
print(maximo)
print(mediana)

grupo = ["Carlos", "Maria", "Bruno", "Maurício", "Thalyta"]
lista = list(grupo)
print(lista)

numeros = [1, 2, 3, 4, 5, 6]
pares = [num % 2 == 0 for num in numeros] 
print(pares)