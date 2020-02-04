from os import path


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


def sair():
    sair = str(input('Deseja sair do programa [sim/não]: ')).strip().lower()
    while sair != 'sim' and sair != 'não':
        print('>>> Digite uma opção válida.')
        sair = str(input('\nDeseja sair do programa [sim/não]: ')).strip().lower()

    if sair == 'não':
        return False

    if sair == 'sim':
        return True


def diretorio(arquivo):
    return path.dirname(path.realpath(__file__)) + '/audio' + '/' + arquivo

