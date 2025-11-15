from models.usuario import Usuario
from models.conta import Conta
import random

def criar_usuario(usuarios):
    nome = input("Insira o nome: ")
    idade = int(input("Insira a idade: "))
    cpf = input("Insira o CPF: ")
    cpf = cpf.replace('.', '').replace('-', '').strip()
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Esse CPF já existe no cadastro.")
        return 
    
    else:
        novo_usuario = Usuario(nome, idade, cpf)
        usuarios.append(novo_usuario)
        return novo_usuario

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, usuarios, contas): 
    from service.conta_service import filtrar_contas
    
    numero_conta = str(random.randint(1, 999999)).zfill(6)
    cpf = input("Insira o CPF: ")
    cpf = cpf.replace('.', '').replace('-', '').strip()
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario: 
        conta_existe = filtrar_contas(cpf, contas)
        
        if conta_existe: 
            print("Usuário já possui conta.")
            return
        
        else:
            nova_conta = Conta(AGENCIA, numero_conta, 0, cpf)
            contas.append(nova_conta)
            print("Conta criada com sucesso: ", nova_conta)
            return nova_conta
    else:
        print("Usuário não encontrado.")
        return 

        
def listar_contas(contas):
    for conta in contas:
        print(conta)
    
    if not contas:
        print("Sem contas registradas no momento.")
