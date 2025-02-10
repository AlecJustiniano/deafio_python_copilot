# Solicitar um texto ao usuário e um inteiro e imprimir a quantidade de vezes no inteiro informado.
# Solicita um texto ao usuário
texto = input("Digite um texto: ")

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Imprime o texto a quantidade de vezes especificada
for i in range(1, numero + 1):
    print(f" {texto}", end=' ')