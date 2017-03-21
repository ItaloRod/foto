# _*_ coding:UTF-8 _*_
from os import mkdir
import cv2
'''
    Programa que recebe o nome da pessoa, cria uma pasta com esse nomes e salva as fotos nessa pasta.
'''
def criarPasta(diretorio):
    try:
        nome = str(raw_input('Nome do usuario: '))
        mkdir(diretorio + "\\" + nome)
        print("Diretorio '%s'criado com sucesso" %nome)
        return diretorio +"\\"+ nome
    except:
        print("Ocorreu um erro. Diretorio ou nome de usuario inválidos")

def informarDiretorio():
    return str(raw_input('Diretorio: '))

def tirarFoto():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val,img = cam.read()
        cv2.imshow('my webcam', img)
        return img

def enviarFoto(diretorio,img):
    arq = open("%s\\x.jpg","w" %diretorio)
    arq.write(img)
    arq.close()

diretorio = None

while(True):
    print("")
    print("** 1 - Tirar Foto")
    print("** 2 - Definir diretorio")
    print("** 3 - Sair")
    menu = int(raw_input('Qual sua escolha: '))
    print("")
    if menu == 1:
        if diretorio != None:
           neodiretorio = criarPasta(diretorio)
           img = tirarFoto()
           enviarFoto(neodiretorio,img)

        else:
            print("ERRO! Preencha o diretorio!")
    elif menu == 2:
        diretorio = informarDiretorio()
    else:
        break