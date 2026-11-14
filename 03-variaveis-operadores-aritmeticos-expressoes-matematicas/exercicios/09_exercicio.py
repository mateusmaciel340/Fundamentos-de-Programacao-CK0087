"""
Exercício 9: prevendo o valor de variáveis encadeadas

Antes de executar, tente prever o valor de cada variável do código abaixo. Depois execute a célula e confira se suas previsões estavam certas.
"""

a = 5
b = a * 2
c = b + a
d = c // 4
e = c % 4

# a = 5, int
print(f"a: {a}")

# b = 5 * 2, b = 10, int
print(f"b: {a} * {2} = {b}")

# c = 10 + 5, c = 15, int
print(f"c: {b} + {a} = {c}")

# d = 15 // 4, d = 3, int
print(f"d: {c} // {4} = {d}")

# e = 15 % 4 => 15 = 4 * 3 + r => r = 15 - 12 => r = 3, e = 3, int
print(f"e: {c} % {4} = {e}")