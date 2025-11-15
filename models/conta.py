class Conta: 
    def __init__(self, agencia, numero_conta, saldo, cpf):
        self.agencia = agencia
        self.numero_conta = numero_conta 
        self.saldo = saldo
        self.cpf = cpf
        self.extrato = []
    
    def __str__(self):
        return "Agência: " + str(self.agencia) + " || Conta: " + str(self.numero_conta) + \
            " || CPF: " + str(self.cpf) + " || Saldo: R$ {:.2f}".format(self.saldo)