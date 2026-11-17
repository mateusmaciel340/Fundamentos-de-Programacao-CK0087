""""
Exercício 14: o que está acontecendo?

Explique o que o código abaixo faz. Teste com vários inteiros `a` e `b`. Depois, justifique por que funciona.
"""

a = 1
b = 200

print(f"Antes da modificação: a = {a}, b = {b}")

# a = 1 + 200 => a = 201
a = a + b
print(f"\na: {1} + {b} = {a}")

# b = 201 - 200 => b = 1
b = a - b
print(f"b: {a} - {200} = {b}")

# a = 201 - 1 => a = 200
a = a - b
print(f"c: {201} - {b} = {a}")

# a = 200, b = 1
print(f"\nDepois da modificação: a = {a}, b = {b}")