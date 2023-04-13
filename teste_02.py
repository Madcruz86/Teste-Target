# Entrada de dados:
num = int(input('Digite um número inteiro: \n'))

# Calculo da sequencia de Fibonacci
fib = [0, 1]
while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

# Mostar sequencia
print(fib)

# Verificar se o número informado pertence a sequencia
if num in fib:
    print(f'Numero {num} pertence à sequência de Fibonacci!')
else:
    print(f'Numero {num} não pertence à sequência de Fibonnaci.')

