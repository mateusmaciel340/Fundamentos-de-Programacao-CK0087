"""
Exercício 4: `x = y` versus `x = 'y'`

Antes de executar, tente prever: o que o código abaixo vai mostrar? Qual é a diferença entre `x = y` e `x = 'y'`?

Execute a célula abaixo e confira se sua previsão estava certa.
"""

y = 3

# x = 3, type(3) => int
x = y
print(f"x = {x} => {type(x)}")

# x = 'y', type('y') => str (string/texto)
x = 'y'
print(f"x = '{x}' => {type(x)}")

"""
O que mudaria se trocássemos `y = 3` por `y = '3'`?

Antes de executar, tente prever. Use a célula abaixo para testar.
"""

y = '3'

# x = '3' => type('3') => str
x = y
print(f"\nx = {x}, {type(x)}")

# x = 'y' => type('y') => str
x = 'y'
print(f"x = {x}, {type(x)}")