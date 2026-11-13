"""
Exercício 2: variáveis e tipos

Crie três variáveis separadas:

1. Uma chamada nome_aluno contendo o nome de uma pessoa (texto).
2. Uma chamada idade_aluno contendo uma idade (número inteiro).
3. Uma chamada estudante_matriculado contendo o valor lógico verdadeiro (booleano)

Em seguida, exiba o tipo de cada uma dessas variáveis utilizando o comando print(type(...)).
"""

nome_aluno = "Mateus"
idade_aluno = 25
estudante_matriculado = True

# nome_aluno => "Mateus" => str
print(f"nome_aluno: {nome_aluno} => {type(nome_aluno)}")

# idade_aluno => 25 => int
print(f"idade_aluno: {idade_aluno} => {type(idade_aluno)}")

# estudante_matriculado => True => bool
print(f"estudante_matriculado: {estudante_matriculado} => {type(estudante_matriculado)}")