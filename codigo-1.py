def is_fibonacci(num):

    def is_perfect_square(x):
        return int(x**0.5)**2 == x

    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
