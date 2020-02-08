from os import path, listdir
from pygame import mixer


def ismp3(arquivo):
    if arquivo[-4:] == '.mp3':
        return True
    else:
        return False


def existeArquivo(arquivo, diretorio):
    if arquivo[-4:] != '.mp3':
        arquivo = arquivo + '.mp3'

    diretorio_audio = path.dirname(path.realpath(__file__)) + '/' + diretorio
    arquivo_diretorio = diretorio_audio + '/' + arquivo

    if path.exists(arquivo_diretorio):
        return True
    else:
        return False


def existeDiretorio(diretorio):
    diretorio_atual = path.dirname(path.realpath(__file__))

    if path.exists(diretorio_atual + '/' + diretorio):
        return True
    else:
        return False


def inexisteArquivo(arquivo):
    if ismp3(arquivo) == True:
        arquivo_inexiste = f'>>> O arquivo "{arquivo}" não foi encontrado.\n>>> Lembre-se: apenas arquivos mp3 são reproduzidos.'
        return arquivo_inexiste
    else:
        musica_inexiste = f'>>> A música "{arquivo}" não foi encontrada.'
        return musica_inexiste


def sair(txt):
    sair = str(input(txt)).strip().lower()
    while sair != 'sim' and sair != 'não':
        print('>>> Digite uma opção válida.\n')
        sair = str(input(txt)).strip().lower()

    if sair == 'sim':
        return True
    else:
        return False


def acabou(txt):
    acabou = str(input(txt)).strip().lower()
    while acabou != 'sim' and acabou != 'não':
        print('>>> Digite uma opção válida.\n')
        acabou = str(input(txt)).strip().lower()

    if acabou == 'não':
        return True
    else:
        return False


def prosseguir(txt):
    prosseguir = str(input(txt)).strip().lower()
    while prosseguir != 'sim' and prosseguir != 'não':
        print('>>> Digite uma opção válida.\n')
        prosseguir = str(input(txt)).strip().lower()

    if prosseguir == 'sim':
        return True
    else:
        return False


def volume(txt):
    print('')
    volume = str(input(txt)).strip()

    while True:
        if not volume.isnumeric():
            print('>>> Digite apenas números inteiros.')
            print('')
            volume = str(input(txt)).strip()
        elif int(volume) not in range(11):
            print('>>> O volume suportado é de 0 a 10.')
            print('')
            volume = str(input(txt)).strip()
        else:
            volume = int(volume)
            break

    return volume


def disponiveis(pasta):
    disponiveis_diretorio = path.dirname(path.realpath(__file__)) + '/' + pasta
    disponiveis_lista = listdir(disponiveis_diretorio)

    return disponiveis_lista


def opcoes():
    opcoes_texto = ('''
========= OPÇÕES =========
 [0] Sair
 [1] Substituir
 [2] Volume
 [3] Alterar volume
 [4] Músicas disponíveis
 [5] Músicas reproduzidas
 [6] Loop
 [7] Reiniciar
 [8] Pausar / Despausar''')
    return opcoes_texto


def opcoes_loop():
    opcoes_loop_texto = ('''
============= OPÇÕES =============
[1] Tocar 1 vez
[2] Tocar 3 vezes
[3] Tocar 4 vezes
[4] Tocar até um próximo reinício''')
    return opcoes_loop_texto


def arquivoFormato(variavel):
    if ismp3(variavel):
        return variavel
    else:
        return variavel + '.mp3'


def musicaFormato(variavel):
    if ismp3(variavel):
        return variavel[:-4]
    else:
        return variavel


def diretorioFormato(pasta, arquivo):
    return path.dirname(path.realpath(__file__)) + '/' + pasta + '/' + arquivo


def tocando():
    if mixer.music.get_pos() == -1:
        return False
    else:
        return True

