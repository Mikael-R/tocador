from os import path, listdir


def ismp3(arquivo):
    if arquivo[-4:] == '.mp3':
        return True
    else:
        return False


def existe(arquivo):
    if arquivo[-4:] != '.mp3':
        arquivo = arquivo + '.mp3'

    diretorio_audio = path.dirname(path.realpath(__file__)) + '/audio'
    arquivo_diretorio = diretorio_audio + '/' + arquivo

    if path.exists(arquivo_diretorio):
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

