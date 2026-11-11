numero1 = 12
numero2 = 5

# 12 + 5 = 17
adicao = numero1 + numero2
print(f"{numero1} + {numero2} = {adicao}")

# 12 - 5 = 7
subtracao = numero1 - numero2
print(f"{numero1} - {numero2} = {subtracao}")

# 12 * 5 = 60
multiplicacao = numero1 * numero2
print(f"{numero1} * {numero2} = {multiplicacao}")

# 12 / 5 = 2.4
divisao = numero1 / numero2
print(f"{numero1} / {numero2} = {divisao}")

divisao_inteira = numero1 // numero2
print(f"{numero1} // {numero2} = {divisao_inteira}")

# 12 % 5 => 12 = 5 * 2 + r => r = 12 - 10, r = 2
resto_divisao = numero1 % numero2
print(f"{numero1} % {numero2} = {resto_divisao}")

exponenciacao = numero1 ** numero2
print(f"{numero1} ** {numero2} = {exponenciacao}")

print("\nUnitários:")

# (-)(-) => + | (+)(-) => -
# (-) + (-) => (-)(-) = +

# -12 - 5 => -17
print(f"{-numero1} - {numero2} = {-numero1 - numero2}")

# -12 + 5 => -7
print(f"{-numero1} + {numero2} = {-numero1 + numero2}")

# 12 -- 5
print(f"{numero1} -- {numero2} = {numero1 -- numero2}")