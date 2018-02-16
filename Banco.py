# encoding: "utf-8"

from datetime import datetime
import os
import sys

# fim import

hora = datetime.now()
print("Agora sao:", hora.hour, "horas", hora.minute, "minutos e", hora.second, "segundos")
# login
print("-----Desenvolvido por Geysom.-----")


def login(logado=True):
    nome = str(input("Insira seu nome: "))
    login_senha = str(input("Insira sua senha: "))
    while nome != 'teste':
        print("Nome incorreto")
        exit()
    while login_senha != 'teste':
        print("Senha incorreta")
        exit()
        return login
    print('-----final do login-----')


login(logado=True)
print("Seja Bem Vindo")
# fim login
# comandos
while True:
    print("O que deseja fazer? ")
    print("1.Criar um arquivo vazio\n"
          "2.Escrever em um arquivo\n"
          "3.Ler arquivo\n"
          "4.Apagar arquivo\n"
          "5.Criptografar\n"
          "6.Descriptografarz\n"
          "99.Sair")
    entrada = input('>')
    if entrada == "1":
        arq = input("Nome do arquivo .txt\n>")
        with open(arq, "a") as dado:
            dado.close()
            continue
    elif entrada == "2":
        arq = input("Em qual arquivo quer escrever?\n>")
        texto = input(":")
        dado = open(arq, "a")
        dado.write("{}\n".format(texto))
        dado.close()
        continue
    elif entrada == "3":
        arq = input("Que arquivo deseja ler?\n>")
        with open(arq, 'r') as dado:
            conteudo = dado.read()
            print("Conteúdo do arquivo\n>")
            print(conteudo)
            continue
    elif entrada == "4":
        arquivo = str(input("digite o nome do arquivo que deseja apagar\n"))
        if arquivo:
            print("---removendo arquivo----")
            os.remove((arquivo))
            continue
    elif entrada == "5":
        def substituir(ind, chave, inicio, fim):
            # tamanho do alfabeto
            n = fim - inicio + 1
            k = (ind + chave) % (fim + 1) + ((ind + chave) // (fim + 1)) * inicio
            if ind + chave < inicio:
                k = k + n
            return chr(k)


        def criptografar(mensagem, chave):
            nA, nZ, na, nz = ord('A'), ord('Z'), ord('a'), ord('z')
            cifrada = ""
            for caracter in mensagem:
                # achar no alfabeto a letra que esteja chave posições a frente
                ind = ord(caracter)
                nova_letra = caracter
                # Se estiver no intervalo de letras maiúsculas
                if nA <= ind <= nZ:
                    nova_letra = substituir(ind, chave, nA, nZ)
                # Outra forma de verificar se está no intervalo de letras (agora) minúsculas
                # lembrar que range gera intervalos da forma [a, b), portanto somamos 1
                elif ind in range(na, nz + 1):
                    nova_letra = substituir(ind, chave, na, nz)

                # substituir na mensagem a letra pela nova_letra
                cifrada = cifrada + nova_letra

            return cifrada


        def descriptografar(mensagem, chave):
            return criptografar(mensagem, -chave)


        def cifrardoc(fonte, destino, chave):
            arquivo = open(fonte, "r")
            conteudo = arquivo.read()
            arquivo.close()
            cifrada = criptografar(conteudo, chave)
            arquivo = open(destino, "w")
            arquivo.write(cifrada)
            arquivo.close()


        def decifrardoc(fonte, destino, chave):
            return cifrardoc(fonte, destino, -chave)


        arq = input("Arquivo para criptografar?\n>")
        with open(arq, 'r') as dado:
            conteudo = dado.read()
        cifrada = criptografar(conteudo, chave=7)
        with open(arq, 'w') as dado:
            conteudo = dado.write("{}\n".format(cifrada))
            dado.close()
            print(cifrada)
            continue
    elif entrada == "6":
        def substituir(ind, chave, inicio, fim):
            # tamanho do alfabeto
            n = fim - inicio + 1
            k = (ind + chave) % (fim + 1) + ((ind + chave) // (fim + 1)) * inicio
            if ind + chave < inicio:
                k = k + n
            return chr(k)


        def criptografar(mensagem, chave):
            nA, nZ, na, nz = ord('A'), ord('Z'), ord('a'), ord('z')
            cifrada = ""
            for caracter in mensagem:
                # achar no alfabeto a letra que esteja chave posições a frente
                ind = ord(caracter)
                nova_letra = caracter
                # Se estiver no intervalo de letras maiúsculas
                if nA <= ind <= nZ:
                    nova_letra = substituir(ind, chave, nA, nZ)
                # Outra forma de verificar se está no intervalo de letras (agora) minúsculas
                # lembrar que range gera intervalos da forma [a, b), portanto somamos 1
                elif ind in range(na, nz + 1):
                    nova_letra = substituir(ind, chave, na, nz)

                # substituir na mensagem a letra pela nova_letra
                cifrada = cifrada + nova_letra

            return cifrada


        def descriptografar(mensagem, chave):
            return criptografar(mensagem, -chave)


        def cifrardoc(fonte, destino, chave):
            arquivo = open(fonte, "r")
            conteudo = arquivo.read()
            arquivo.close()

            cifrada = criptografar(conteudo, chave)

            arquivo = open(destino, "w")
            arquivo.write(cifrada)
            arquivo.close()


        def decifrardoc(fonte, destino, chave):
            return cifrardoc(fonte, destino, -chave)


        arq = input("Arquivo para descriptografar\n>")
        with open(arq, 'r') as dado:
            conteudo = dado.read()
            dado.close()
            decifrar = descriptografar(conteudo, chave=7)
        with open(arq, 'w') as dado:
            dado.write(decifrar)
            continue
    elif entrada == "99":
        sys.exit(0)

# fim comandos
