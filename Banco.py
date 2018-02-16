from datetime import datetime
import os

hora = datetime.now()
print("Agora são:", hora.hour, "horas", hora.minute,"minutos e",hora.second,"segundos")
#login
print("-----Login-----")
def login(logar):
    login = str(input("Insira seu nome: "))
    login_senha = str(input("Insira sua senha: "))
    while login != "algum nome aqui":
        print("Nome incorreto")
        break
    while login_senha != "alguma senha aqui":
        print("Senha incorreta")
        exit()
        return login
    print('-----final do login-----')
    print('Seja Bem Vindo %s' % (login))
login(logar=0)
print("O que deseja fazer? ")
print("1.Criar um arquivo vazio\n"
      "2.Escrever em um arquivo\n"
      "3.Ler arquivo\n"
      "4.Apagar arquivo")
entrada = input('>')

while(entrada == "0"):
    print("Adeus.")
    exit()
else:

    if entrada == "1":
        arq = input("Nome do arquivo .txt\n>")
        with open(arq, "a") as dado:
            dado.close()
    elif entrada == "2":
        arq = input("Em qual arquivo quer escrever?\n>")
        texto = input(":")
        dado = open(arq, "a")
        dado.write("{}\n".format(texto))
        dado.close()
    elif entrada == "3":
        arq = input("Que arquivo deseja ler?\n>")
        with open(arq, 'r') as dado:
            dado = dado.read()
            print("Conteúdo do arquivo\n>")
            print(dado)
    elif entrada == "4":
        arquivo = str(input("digite o nome do arquivo que deseja apagar\n"))
        if arquivo:
            print("---removendo arquivo----")
            os.remove((arquivo))