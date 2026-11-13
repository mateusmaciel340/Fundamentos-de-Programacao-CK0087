preco = 100.0
print(f"Preço atual: R$ {preco}")

# 100.0 + 10.0 => 110.0
preco += 10.0
print(f"Preço atual [R$ {preco}] + Frete [R$ {10.0}] = R$ {preco}")

# 110.0 * 1.05 => 110.0 * 105 / 100 => 11 * 105 / 10 => 11 * 21 / 2 => 231 / 2 => 115.5
preco *= 1.05
print(f"Preço atual [R$ {110.0}] * Taxa [R$ {1.05}] => R$ {preco}")

# 115.5 - 15.00 => 100.5
preco -= 15.00
print(f"Preço atual [R$ {115.5}] - Cupom de desconto [R$ {15.00}] = R$ {preco}")