nome_usuario = "rafaela"
idade_usuario = 30
altura_usuario = 1.85
status_usuario = True

print(f"nome_usuario: {nome_usuario} => {type(nome_usuario)}")
print(f"idade_usuario: {idade_usuario} => {type(idade_usuario)}")
print(f"altura_usuario: {altura_usuario} => {type(altura_usuario)}")
print(f"status_usuario: {status_usuario} => {type(status_usuario)}")

print("\nImportante:")
numero = 35
numero_texto = "35"
print(f"numero: {numero} => {type(numero)}")
print(f"numero_texto: '{numero_texto}' => {type(numero_texto)}")

print(f"{numero} != '{numero_texto}'? {numero != numero_texto}")
print(f"{numero} == '{numero_texto}'? {numero == numero_texto}")

booleano = True
booleano_texto = "True"
print(f"\nbooleano: {booleano}")
print(f"booleano_texto: '{booleano_texto}'")

print(f"{booleano} != {booleano_texto}? {booleano != booleano_texto}")
print(f"{booleano} == {booleano_texto}? {booleano == booleano_texto}")