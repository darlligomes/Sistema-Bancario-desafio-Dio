from service.conta_service import depositar, sacar, exibir_extrato, filtrar_contas
from service.usuario_service import criar_usuario, criar_conta, listar_contas

AGENCIA = "0001"
LIMITES_SAQUES = 3

usuarios = []
contas = []

def menu():
    print("Opções:")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[nc] Nova Conta")
    print("[lc] Listar contas")
    print("[nu] Novo Usuário")
    print("[q] Sair")
    return input("Escolha uma opção: ")

def main():
    numero_saques = 0
    limite = 500

    while True:
        opcao = menu().lower()

        if opcao == "d":
            cpf = input("CPF: ")
            conta = filtrar_contas(cpf, contas)
            if conta:
                valor = float(input("Valor do depósito: "))
                depositar(conta, valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "s":
            cpf = input("CPF: ")
            conta = filtrar_contas(cpf, contas)
            if conta:
                valor = float(input("Valor do saque: "))
                numero_saques = sacar(conta, valor, limite, numero_saques, LIMITES_SAQUES)
            else:
                print("Conta não encontrada.")

        elif opcao == "e":
            cpf = input("CPF: ")
            conta = filtrar_contas(cpf, contas)
            if conta:
                exibir_extrato(conta)
            else:
                print("Conta não encontrada.")

        elif opcao == "nc":
            criar_conta(AGENCIA, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            print("Saindo...")
            break
        
        else: 
            menu().lower()


if __name__ == "__main__":
    main()
