while True:
    # Solicita dois números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Solicita a operação matemática desejada
    operacao = input("Digite a operação matemática desejada (adição, subtração, multiplicação, divisão): ").strip().lower()

    # Realiza o cálculo com base na operação informada
    if operacao == 'adição':
        resultado = num1 + num2
    elif operacao == 'subtração':
        resultado = num1 - num2
    elif operacao == 'multiplicação':
        resultado = num1 * num2
    elif operacao == 'divisão':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero não é permitida."
    else:
        resultado = "Operação inválida."

    # Imprime o resultado
    print(f"O resultado da operação é: {resultado}")

    # Pergunta ao usuário se deseja continuar
    continuar = input("Deseja realizar outra operação? (sim/não): ").strip().lower()
    if continuar != 'sim':
        print("Encerrando o programa.")
        break