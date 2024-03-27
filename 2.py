#Radix question 2

"""Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência."""

############################################################################################################################

#CODE:

def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    return fibonacci

def check(number, sequence):
    if number in sequence: return True
    return False

number = int(input("Enter a number to check if it belongs to the Fibonacci sequence: "))
fibonacci_sequence = fibonacci_sequence(number)

if check(number, fibonacci_sequence):
    print(f"'{number}' belongs to the Fibonacci sequence.")
else:
    print(f"'{number}' does not belong to the Fibonacci sequence.")