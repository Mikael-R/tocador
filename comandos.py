from os import path, listdir


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


def sair(txt):
    sair = str(input(txt)).strip().lower()
    while sair != 'sim' and sair != 'não':
        print('>>> Digite uma opção válida.')
        print('')
        sair = str(input(txt)).strip().lower()

    if sair == 'não':
        return False

    if sair == 'sim':
        return True


def diretorio(arquivo):
    return path.dirname(path.realpath(__file__)) + '/audio' + '/' + arquivo


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
======= OPÇÕES =======
[0] Sair
[1] Substituir
[2] Loop
[3] Reiniciar
[4] Pausar / Despausar
[5] Volume
[6] Alterar volume
[7] Música atual
[8] Músicas reproduzidas
[9] Músicas disponíveis''')
    return opcoes_texto


def opcoes_loop():
    opcoes_loop_texto = ('''
========== OPÇÕES ==========
[1] Tocar 1 vez
[2] Tocar 3 vezes
[3] Tocar 4 vezes
[4] Tocar até um próximo reinício''')
    return opcoes_loop_texto

