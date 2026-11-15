"""
Exercício 12: Extraindo e remontando dígitos

Dado o número `847`, use os operadores `//` e `%` para:

1. Extrair o dígito das centenas (8), o das dezenas (4) e o das unidades (7).
2. Calcular a soma dos dígitos (8 + 4 + 7 = 19).
3. Construir o número invertido (748).

Seu código deve funcionar para qualquer número de 3 dígitos. Teste trocando `847` por `123` e depois por `905`.
"""

numero = 847
print(f"* Número inicial: {numero}\n")

"""
Centena => 847 // 100 => 8 * 100 = 800, [8]
Dezena => 847 % 100 => 847 = 100 * 8 + r => r = 847 - 800 = 47
          (847 % 100) // 10 => 47 // 10 = 10 * 4 = 40
          
Unidade => 847 % 100 => 47 % 10 => 47 = 10 * 4 + r => r = 47 - 40, r = 7
"""

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10

numero_completo = int(f"{centena}{dezena}{unidade}")
print(f"1) Número completo (c/d/u): {numero_completo}")

soma_digitos = centena + dezena + unidade
print(f"2) Soma de dígitos: {centena} + {dezena} + {unidade} = {soma_digitos}")

# centena = 8, dezena = 4, unidade = 7 => 847
# centena = 7, dezena = 4, unidade = 8 => 748
constante_separacao = unidade

unidade = centena
centena = constante_separacao

numero_completo = int(f"{centena}{dezena}{unidade}")
print(f"3) Número completo (c/d/u) - invertido: {numero_completo}")