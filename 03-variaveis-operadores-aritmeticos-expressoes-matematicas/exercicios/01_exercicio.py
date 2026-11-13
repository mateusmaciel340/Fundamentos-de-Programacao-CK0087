"""
Exercício 1: Nomes de variáveis

Item A) Dentre as opções de nome abaixo, escolha o único válido como identificador de variável e crie uma variável com tal nome (o valor da variável pode ser um número qualquer).

* 1_nota
* nota final
* nota_final
* nota-final
* nota#final
"""

nota_final = (8.5 + 2.0) / 2
print(f"Item A) ({8.5} + {2.0}) / {2} = {nota_final}")

# não válida => 1_nota, nota final, nota-final, nota#final

"""
O nome `oi?` não é válido como identificador de variável no Python.
O código abaixo dará erro? Justifique sua resposta mentalmente antes de executar.
"""

# Resposta => Não, uma string (texto => str) normal

nome = "oi?"
print("Item B)",nome)