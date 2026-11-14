""""
Exercício 10: operadores aritméticos

Siga as instruções da célula de código para responder às perguntas.

* Em cada item, substitua 'Substitua aqui' por uma expressão matemática.
* Não introduza variáveis nesta célula de código.
* Não responda mentalmente, use os operadores aritméticos!
"""

def exibirTitulo(titulo):
    print("="*60)
    print(f"\n{titulo})")

"""
Item A: Uma pesquisa de campo tem 100 questionários para serem separados em pilhas de 11.
Quantas pilhas completas serão formadas? Quantos questionários sobram?
"""

quantidade_questionarios = 100
pilhas_separadas = 11

# 100 // 11 => 11 * 10 => 110, 11 * [9] => 99, pilhas_completas = 9
pilhas_completas = quantidade_questionarios // pilhas_separadas

# 100 = 11 * 9 + r => r = 100 - 99 => r = 1
questionarios_sobra = quantidade_questionarios % pilhas_separadas

exibirTitulo("Item A")
print(f"Quantidade de questionários: {quantidade_questionarios}")
print(f"Pilhas separadas: {pilhas_separadas}")

print(f"\nPilhas completas: {pilhas_completas}")
print(f"Questionários que sobraram: {questionarios_sobra}")

"""
Item B: Uma prova tem 60 questões e uma pessoa
precisa acertar 70% delas para ser aprovada.
Quantas questões ela precisa acertar?
"""

quantidade_questoes = 60
percentual_acerto = 0.7
quantidade_minima_aprovacao = int(quantidade_questoes * percentual_acerto)
quantidade_minima_erros = quantidade_questoes - quantidade_minima_aprovacao

exibirTitulo("Item B")
print(f"Quantidade de questões: {quantidade_questoes}")
print(f"Quantidade mínima de questões (aprovação): {quantidade_minima_aprovacao}")
print(f"Quantidade mínima de erros: {quantidade_minima_erros}")

"""
Item C: A nota final de uma disciplina é calculada pela média aritmética de 3 notas.
Calcule a nota final de uma pessoa que tirou notas 7.5, 9 e 6, respectivamente.
"""

primeira_nota = 7.5
segunda_nota = 9
terceira_nota = 6

nota_final = (primeira_nota + segunda_nota + terceira_nota) / 3

exibirTitulo("Item C")
print(f"Nota1: {primeira_nota} / Nota2: {segunda_nota} / Nota3: {terceira_nota}")
print(f"Nota final: ({primeira_nota} + {segunda_nota} + {terceira_nota}) / {3} = {nota_final}")

"""
Item D: Uma população de 100 indivíduos dobra de tamanho a cada ano.
Qual será o tamanho da população após 3 anos? E após 10 anos?
"""

tamanho_populacao = 100
constante_criterio = 2

exibirTitulo("Item D")
print(f"Tamanho inicial da população: {tamanho_populacao}")

tempo = 3
tamanho_populacao *= constante_criterio ** tempo
print(f"Tamanho da população (após {tempo} anos): {tamanho_populacao}")

tempo = 7
tamanho_populacao *= constante_criterio ** tempo
print(f"Tamanho da população (após {tempo} anos): {tamanho_populacao}")

"""
Item E: O número 10 é par e o número 7 é ímpar.
Calcule o resto da divisão de cada um por 2.
"""

numero_par, numero_impar = 10, 7
constante = 2

resto_numero_par_por_dois = numero_par % constante
resto_numero_impar_por_dois = numero_impar % constante

exibirTitulo("Item E")

# 10 = 2 * 5 + r => r = 10 - 10, r = 0
print(f"{numero_par} % {constante} = {resto_numero_par_por_dois}")

# 7 = 2 * 3 + r => r = 7 - 6 => r = 1
print(f"{numero_impar} % {constante} = {resto_numero_impar_por_dois}")

"""
Item F: O IMC (Índice de Massa Corporal) é calculado
dividindo a massa em kg pela altura ao quadrado em metros.
Calcule o IMC de uma pessoa com 70 kg e 1m e 70cm de altura.
"""

peso, altura = 70, 1.70
imc = peso / altura ** 2

exibirTitulo("Item F")
print(f"Peso: {peso}kg / Altura: {altura}cm")
print(f"IMC: {imc}")

"""
Item G: Um produto custa R$ 80,00 e está com 25% de desconto.
Qual o valor do desconto? Qual o preço final?
"""

exibirTitulo("Item G")

preco_produto = 80.00
print(f"Preço do produto: R$ {preco_produto}")

percentual_desconto = 0.25
preco_desconto = preco_produto * percentual_desconto
print(f"Preço descontado: R$ {preco_desconto}")

preco_produto -= preco_desconto
print(f"Preço final: R$ {preco_produto}")

"""
Item H: Um ônibus percorreu 90 km em 1,5 h.
Qual a velocidade média em km/h? E em m/s?
"""

distancia, tempo = 90, 1.5
velocidade_media_km_h = distancia / tempo

exibirTitulo("Item H")
print(f"velocidade_media_km_h: {distancia}km / {tempo}h = {velocidade_media_km_h}km/h")

distancia = distancia * 10 ** 3
tempo = tempo * 3600
velocidade_media_m_s = velocidade_media_km_h / 3.6

print(f"velocidade_media_m_s: {distancia}m / {tempo}s = {velocidade_media_m_s}m/s")

"""
Item I: Quantos segundos tem 1 ano? Considere 1 ano = 365 dias.
"""

segundos, minutos, horas, dias = 60, 60, 24, 365
quantidade_segundos_dias = segundos * minutos * horas * dias

exibirTitulo("Item I")
print(f"Um ano ({dias} dias) tem {quantidade_segundos_dias} segundos")