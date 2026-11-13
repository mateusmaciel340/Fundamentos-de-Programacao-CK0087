numero_total_pessoas = 148
numero_pessoas_por_grupo = 7

grupos_completos = numero_total_pessoas // numero_pessoas_por_grupo
pessoas_fora = numero_total_pessoas % numero_pessoas_por_grupo

print(f"Número total de pessoas: {numero_total_pessoas}")
print(f"Número de pessoas por grupo: {numero_pessoas_por_grupo}")

print(f"\nGrupos completos: {grupos_completos}")
print(f"Pessoas de fora (grupos completos): {pessoas_fora}")