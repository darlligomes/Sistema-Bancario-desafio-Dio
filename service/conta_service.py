from models.conta import Conta
from datetime import datetime
mensagem: str = ''

def depositar(conta, valor: float, /):
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    mensagem = f"[{horario}]- Depósito no valor de R$ {valor:.2f}"
    conta.saldo += valor 
    conta.extrato.append(mensagem)
    print(mensagem)
    return
    
def sacar(conta, valor: float, limite, numero_saques, LIMITES_SAQUES):
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if valor > 0:
        if valor > conta.saldo:
            mensagem = f"[{horario}] Erro na operação de saque no valor de {valor:.2f}. Valor solicitado maior que o saldo atual da conta."
            print(mensagem)
            conta.extrato.append(mensagem)
            return
        
        if valor > limite: 
            print("Valor do saque excede o limite permitido.")
            return numero_saques
        
        if numero_saques >= LIMITES_SAQUES:
            print("Número máximo de saques atingido.")
            return numero_saques
        
        conta.saldo -= valor
        mensagem = f"[{horario}] Saque de valor {valor:.2f} feito com sucesso."
        conta.extrato.append(mensagem)
        print(mensagem)
        
        return numero_saques + 1
    else: 
        print("Valor deve ser acima de 0.")
        return

def exibir_extrato(conta):
    if not conta.extrato:
        print("Nenhuma movimentação registrada.")
    else:    
        print("Extrato: \n")
        for msg in conta.extrato:
            print(f"{msg}\n")
        print(f"Saldo atual: {conta.saldo:.2f}")
    

def filtrar_contas(cpf, contas):
    contas_filtradas = [conta for conta in contas if conta.cpf == cpf]
    return contas_filtradas[0] if contas_filtradas else None
