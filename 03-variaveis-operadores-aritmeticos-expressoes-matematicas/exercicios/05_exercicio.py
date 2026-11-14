"""
Exercício 5: prevendo tipos

Antes de executar, escreva em um comentário qual tipo você acha que cada valor abaixo tem. Depois use `print(type(...))` para conferir.

Valores:

* 7
* "7"
* 7.0
* "sete"
* True
* "True"
"""

# 7 => type(7) => int
ex5_1 = 7
print(f"{ex5_1} => {type(ex5_1)}")

# "7" => type("7") => str
ex5_2 = "7"
print(f"{ex5_2} => {type(ex5_2)}")

# 7.0 -> type(7.0) => float
ex5_3 = 7.0
print(f"{ex5_3} => {type(ex5_3)}")

# "sete" => type("sete") => str
ex5_4 = "sete"
print(f"{ex5_4} => {type(ex5_4)}")

# True => type(True) => bool
ex5_5 = True
print(f"{ex5_5} => {type(ex5_5)}")

# "True" => type("True") => str
ex5_6 = "True"
print(f"{ex5_6} => {type(ex5_6)}")