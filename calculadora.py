def calculadora():
    while True:
        print(" calculadora simples")
        print()
        print("1. soma")
        print("2. subtraçao")
        print("3. multiplacacao")
        print("4. divisao")
        print("s. Sair")
        operacao = input("Selecione uma opcao ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("obrigado por utilizar a calculadora simples ")
            break

        if operacao not in ['1', '2', '3', "4"]:
            print("opcao invalida! tente novamente.")
            continue

        numero_1 = float(input("primeiro numero "))
        numero_2 = float(input("segundo numero "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("o resultado da operacao soma é:", resultado)

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("o resultado da operacao subtracao  é:", resultado)

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("o resultado da operacao multiplicacao é:", resultado)
        else :
            if numero_2 == 0:
                print("divisoes por zero nao sao possiveis.")
                continue
            else:
                resultado = numero_1 / numero_2
            print("o resultado da operacao divisao é:", resultado)
calculadora()