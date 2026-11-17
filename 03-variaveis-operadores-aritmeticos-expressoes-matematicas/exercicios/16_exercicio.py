"""
Exercício 16: Caixa eletrônico

Um caixa eletrônico precisa sacar o valor de R$ 287,00 usando o menor número possível de cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2 e R$ 1.

Use // e % para calcular quantas cédulas de cada valor serão entregues.

Seu código deve funcionar para qualquer valor inteiro. Teste com 287, depois com 153 e 1000.
"""

valor = 287.00

# 100 * 2 = 200.0 + 87.0 => R$ 287.00
cedula = 100
print(
    f"Quantidade de cédulas (R$ {cedula}) entregues: {int(valor // cedula)}",
    f"Sobra: R$ {valor % cedula}", sep=" / "
)

# 50 * 5 => 250.0 + 37.0 => R$ 287.00
cedula = 50
print(
    f"Quantidade de cédulas (R$ {cedula}) entregues: {int(valor // cedula)}",
    f"Sobra: R$ {valor % cedula}", sep=" / "
)

# 20 * 14 => 280.0 + 7.0 => R$ 287.0
cedula = 20
print(
    f"Quantidade de cédulas (R$ {cedula}) entregues: {int(valor // cedula)}",
    f"Sobra R$ {valor % cedula}", sep=" / "
)

# 10 * 28 => 280.0 + 7.0 => R$ 287.0
cedula = 10
print(
    f"Quantidade de cédulas (R$ {cedula}) entregues: {int(valor // cedula)}",
    f"Sobra R$ {valor % cedula}", sep=" / "
)

# 5 * 57 => 285.0 + 3.0 => R$ 287.0
cedula = 5
print(
    f"Quantidade de cédulas (R$ {cedula}) entregues: {int(valor // cedula)}",
    f"Sobra R$ {valor % cedula}", sep=" / "
)

# 2 * 143 => 286.0 + 1.0 => R$ 287.0
cedula = 2
print(
    f"Quantidade de cédulas (R$ {cedula}) entregues: {int(valor // cedula)}",
    f"Sobra R$ {valor % cedula}", sep=" / "
)

cedula = 1
print(
    f"Quantidade de cédulas (R$ {cedula}) entregues: {int(valor // cedula)}",
    f"Sobra R$ {valor % cedula}", sep=" / "
)