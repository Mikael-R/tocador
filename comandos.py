from os import path, listdir, system, name
from pygame import mixer

diretorio_atual = path.dirname(path.realpath(__file__))
diretorio_audio = diretorio_atual + '/' + 'audio'
formatos = ['.mp3', '.mp4', '.wma', '.aac', '.pcm', '.ac3', '.mov']

# VERIFICAÇÕES #
def musicaTocando():
    if mixer.music.get_pos() == -1:
        return False
    else:
        return True


def musicaFormato(musica, diretorio=diretorio_audio):
    try:
        for formato in formatos:
            if musica[-4:] != formato:
                arquivo = musica + formato
                musica_diretorio = diretorio + '/' + arquivo
                if path.exists(musica_diretorio):
                    musica_formato = formato
                    break
            else:
                arquivo = musica
                musica_diretorio = diretorio + '/' + arquivo
                if path.exists(musica_diretorio):
                    musica_formato = formato
                    break
        return musica_formato
    except UnboundLocalError:
        return 'NONE'


def musicasDisponiveis(diretorio=diretorio_audio):
    try:
        disponiveis_lista = listdir(diretorio)
        return disponiveis_lista
    except FileNotFoundError:
        return 'NONE'


def musicaDuplicada(musica, diretorio=diretorio_audio):
    cont = 1
    if musica[-4:] == musicaFormato(musica):
        musica = musica[-4:]
    for formato in formatos:
        arquivo = musica + formato
        diretorio_arquivo = diretorio + '/' + arquivo
        if path.exists(diretorio_arquivo):
            cont += 1
    if cont > 2:
        return True
    else:
        return False

def musicaExiste(musica, diretorio=diretorio_audio):
    if musica[-4:] != musicaFormato(musica):
        arquivo = musica + musicaFormato(musica)
    else:
        arquivo = musica
    diretorio_arquivo = diretorio + '/' + arquivo
    if path.exists(diretorio_arquivo):
        return True
    else:
        return False


def musicaInexiste(arquivo):
    for formato in formatos:
        if arquivo[-4:] == formato:
            inexiste_txt = f'>>> O arquivo "{arquivo}" não foi encontrado.'
            break
        else:
            inexiste_txt = f'>>> A música "{arquivo}" não foi encontrada.'

    return inexiste_txt

# TEXTOS #
def limpar():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


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

    return volume / 10


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


def opcoesLoop():
    opcoes_loop_texto = ('''
============= OPÇÕES =============
[1] Tocar 3 vezes
[2] Tocar 4 vezes
[3] Tocar até um próximo reinício''')
    return opcoes_loop_texto

# FORMATAÇÕES #
def arquivoFormatado(musica):
    if musica[-4:] == musicaFormato(musica):
        return musica
    else:
        return musica + musicaFormato(musica)


def musicaFormatada(musica):
    if musica[-4:] == musicaFormato(musica):
        return musica[:-4]
    else:
        return musica


def diretorioFormatado(arquivo, diretorio=diretorio_audio):
    return diretorio + '/' + arquivo

