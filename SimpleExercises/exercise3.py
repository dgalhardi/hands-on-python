from sys import getsizeof

# Generator Expressions
# Uma forma mais rapida para listas, dicionarios e etc
# menos memoria alocada
# valores em bytes

numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
print(getsizeof(numeros))

numeros = (x * 10 for x in range(1000000))
print(type(numeros))
print(getsizeof(numeros))