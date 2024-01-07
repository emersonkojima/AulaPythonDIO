#implementar deposito, saque e extrato
#Operadores do MENU
opcao_menu = "a"
contador = True

#Operadores da CONTA
saldo = 500.00
saque = 0.0
contador_saque_diario = 0
registro_de_operacoes_saque = []
registro_de_operacoes_deposito = []

try:
    while contador == True:
        opcao_menu=input('''                    ###########  SELECIONE UMA OPÇÃO  ###########

                    |           -(D) Para DEPOSITO              |
                    |           -(S) Para SAQUE                 |
                    |           -(E) Para EXTRATO               |
                    |           -(Q) Para SAIR                  |

                    #############################################

                         ''').upper()
    
        if opcao_menu == "Q":
            contador = False

        elif opcao_menu == "D":
            deposito = float(input("Informe o valor você deseja depositar? "))
            if deposito > 0:
                saldo = saldo + deposito
                registro_de_operacoes_deposito.append(deposito)
                print(f"Procedimento realizado com SUCESSO!!!\nSEU NOVO SALDO É ---------> : {saldo}\n")
            else:
                print("O valor depositado não pode ser negativo")

        elif opcao_menu == "S":
            saque=float(input("Qual o valor que deseja sacar? "))
            if saque <= saldo and contador_saque_diario < 3 and saque <= 500 and saque > 0: 
                print("saque autorizado".upper())
                saldo = saldo - saque
                contador_saque_diario +=1
                registro_de_operacoes_saque.append(saque)
                print(f"Saldo atual ---------> R$ {saldo}".title())
                
            elif contador_saque_diario == 3:
                print(f"Numeros de saque diario excedido - Foram realizados {contador_saque_diario} saques")
                print("Tente novamente amanhã ou fale com seu gerente")
            elif saque > saldo:
                print("Saldo insuficiente".upper())
            elif saque > 500:
                print("Só pode ser realizados saques de no maximo R$ 500 por vez")
                print("Caso precise de valores superiores, realize uma nova operação.")
            else:
                print("O saque não pode conter numeros negativos, verifique e tente novamente")

        elif opcao_menu == "E":    
            print(f"Saldo atual ---------> R$ {saldo}".title())
            print("A quantidades de saques realizados foi :", contador_saque_diario)
            depositos_formatados = ["R${:.2f}".format(valor) for valor in registro_de_operacoes_deposito]
            print("Depósitos realizados em REAIS: ", depositos_formatados)
            print("")
            saques_formatados = ["R${:.2f}".format(valor) for valor in registro_de_operacoes_saque]
            print("Saques realizados em REAIS: ", saques_formatados)
            print("")
        else:
             print("---------- Operação desconhecida, tente novamente ----------\n".upper())
except ValueError:
    print("Ocorreu um ERRO - Por favor, tente novamente mais tarde :(")
