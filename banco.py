menu = """
    [d] Depositar
    [s] Sacar
    [e] Conferir Extrato
    [q] Sair
"""

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado \n"))

        if valor_deposito < 0:
            print("Não é possível depositar números negativos \n")
        else:
            saldo += valor_deposito
            print("Depósito Concluído com sucesso \n")
            extrato += f"Depósito: R${valor_deposito:.2f}\n"

    elif opcao == "s":
        valor_saque = float(input("Digite o valor a ser sacado \n"))

        if valor_saque > LIMITE: 
            print("Erro, você não pode sacar mais de 500 reais.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Erro, você não pode sacar mais de 3 vezes.")
        elif valor_saque > saldo:
            print("Erro, você não tem dinheiro o bastante.")
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Depósito: R${valor_saque:.2f}\n"

    elif opcao == "e":
        print("\n=============EXTRATO=============")
        print("Não há registros." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print(f"Você ainda pode realizar {LIMITE_SAQUES - numero_saques} saques.")
        print("\n=================================")

    elif opcao == "q":
        print("Sistema Encerrado")
        break

    else:
        print("Operação Inválida")
