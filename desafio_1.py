'''
**********************************************
Olavo Borges D'Antonio

DIO - curso de Python

**********************************************
'''
menu = """
    **** MENU ****
    
    (d) -> DEPOSITO
    (e) -> EXTRATO
    (s) -> SAQUE
    (0) -> SAIR
    
    **************
"""

saldo = 0
saque = 0
valor_deposito = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3
limite_saque = 500

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Operação Depósito\n")
        valor_deposito = float(input("Entre com o valor a ser depositado: "))
        if valor_deposito > 0:
            print("Operação realizada com sucesso.")
            saldo = saldo + valor_deposito
            extrato = extrato + f"Deposito no valor de R$ {valor_deposito:.2f}\n"
        else:
            print("Falha na operação.")
    elif opcao == "s":
        print("Saque")
        if numero_saques <= LIMITE_SAQUES_DIARIO:
            saque = float(input("Digite o valor: "))
            if saque > 0:
                if saque <= saldo:
                    if saque <= limite_saque:
                        saldo = saldo - saque
                        numero_saques = numero_saques + 1
                        extrato = extrato + f"Saque no valor de R$ {saque:.2f}\n"
                        print("Operação realizada com sucesso.")
                    else:
                        print("Valor do saque acima do limite.")
                else:
                    print("Saldo Insuficiente.")
            else:
                print("Falha na operação.")
        else:
            print("Limite de saques diarios atingido.")
            
    elif opcao == "e":
        print("Extrato da Conta")
        if not extrato:
            print("Não foram encontradas movimentaçõe.")
            print(f"O saldo total é de R$ {saldo:.2f}")
        else:
            print(extrato)
            print(f"Saldo total é de R$ {saldo:.2f}")
        
    elif opcao == "0":
        print("Finalizando")
        break
    
    else:
        print("Opção selecionada não é uma operação válida, por favor selecione uma operação válida.")


