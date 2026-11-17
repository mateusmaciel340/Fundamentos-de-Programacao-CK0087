"""
Exercício 15: Prevendo tipos de expressões

Antes de executar, escreva em comentários qual **tipo** cada expressão produz. Depois confira com `print(type(...))

a) 10 / 2
b) 10 // 2
c) 10 % 2
d) 2 ** 0.5
e) 7 + 3.0
f) "7" + "3"
"""

# 10 / 2 => 5.0 (float)
a = 10 / 2
print(f"a) {10} / {2} = {a} ({type(a)})")

# 10 // 2 = 5 (int)
b = 10 // 2
print(f"b) {10} // {2} = {b} ({type(b)})")

# 10 % 2 => 10 = 2 * 5 + r => r = 10 - 10 => r = 0, c = 0 (int)
c = 10 % 2
print(f"c) {10} % {2} = {c} ({type(c)})")

# 2 ** 0.5 => 2 ** 1/2 => \sqrt{2} => 1.???? (float)
d = 2 ** 0.5
print(f"d) {2} ** {0.5} = {d} ({type(d)})")

# 7 + 3.0 => 10.0 (float)
e = 7 + 3.0
print(f"e) {7} + {3.0} = {e} ({type(e)})")

# "7" + "3" => "73" (str)
f = "7" + "3"
print(f"'{"7"}' + '{"3"}' = {f} ({type(f)})")

"""
Por que 10 / 2 e 10 // 2 têm tipos diferentes, mesmo ambos valendo 5?

10 / 2 => 5.0 (processo de divisão completa, contabilizando as casas decimais).
10 // 2 => 5 (processo de divisão inteira, ignorando o que não é inteiro).
"""

