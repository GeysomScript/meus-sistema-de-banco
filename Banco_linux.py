from datetime import datetime
import os

hora = datetime.now()
print("Agora são:", hora.hour, "horas", hora.minute,"minutos e",hora.second,"segundos")
#login
print('\033[35m'+'-----Login-----'+'\033[0;0m')
def login(logar):
    login = str(input( '\033[31m'+'Insira seu nome: '+'\033[0;0m'))
    login_senha = str(input('\033[31m'+'Insira sua senha: '+'\033[0;0m'))
    while login != "login":
        print("Nome incorreto")
        break
    while login_senha != "senha":
        print("Senha incorreta")
        exit()
        return login
    print('\033[35m'+'-----final do login-----'+'\033[0;0m')
    print('Seja Bem Vindo %s' % (login))
login(logar=0)
print('\033[44m'+'O que deseja fazer? '+'\033[0;0m')
print("1.Criar um arquivo vazio\n"
      "2.Escrever em um arquivo\n"
      "3.Ler arquivo\n"
      "4.Apagar arquivo")
entrada = input('\033[33m'+'> '+'\033[0;0m')

while(entrada == "0"):
    print("Adeus.")
    exit()
else:

    if entrada == "1":
        arq = input('\033[35m'+'Nome do arquivo .txt\n>'+'\033[0;0m')
        with open(arq, "a") as dado:
            dado.close()
    elif entrada == "2":
        arq = input('\033[35m'+'Em qual arquivo quer escrever?\n>'+'\033[0;0m')
        texto = input(":")
        dado = open(arq, "a")
        dado.write("{}\n".format(texto))
        dado.close()
    elif entrada == "3":
        arq = input('\033[35m'+'Que arquivo deseja ler?\n>'+'\033[0;0m')
        with open(arq, 'r') as dado:
            dado = dado.read()
            print('\033[35m'+'Conteúdo do arquivo\n>'+'\033[0;0m')
            print(dado)
    elif entrada == "4":
        arquivo = str(input('\033[35m'+'digite o nome do arquivo que deseja apagar\n'+'\033[0;0m'))
        if arquivo:
            print('\033[41m'+'---removendo arquivo----'+'\033[0;0m')
            os.remove((arquivo))
