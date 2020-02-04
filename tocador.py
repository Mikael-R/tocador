from pygame import mixer
from os import listdir
from os import path
import comandos

playlist = list()
opcoes = ('''
======= OPÇÕES =======
[0] Sair
[1] Substituir
[2] Loop
[3] Reiniciar
[4] Pausar / Despausar
[5] Volume
[6] Alterar volume
[7] Nome
[8] Músicas reproduzidas
[9] Músicas disponíveis''')
opcoes_loop = ('''
========== OPÇÕES ==========
[1] Tocar 1 vez
[2] Tocar 3 vezes
[3] Tocar 4 vezes
[4] Tocar até um próximo reinício''')

mixer.init()

while True:
    musica = str(input('\nQual música deseja ouvir: ')).strip()
    while musica == '':
        print('>>> Digite algo.')
        print('>>> Lembre-se: apenas arquivos mp3 são reproduzidos.')
        musica = str(input('\nQual música deseja ouvir: ')).strip()

    if comandos.existe(musica) == True:
        if comandos.ismp3(musica) ==  True:
            arquivo = musica
            musica = musica[:-4]
            diretorio = comandos.diretorio(arquivo)
            break
        else:
            arquivo = musica + '.mp3'
            diretorio = comandos.diretorio(arquivo)
            break

    if comandos.existe(musica) == False:
        if comandos.ismp3(musica) == True:
            print(f'>>> O arquivo "{musica}" não foi encontrado.')
        else:
            print(f'>>> A música "{musica}" não foi encontrada.')

mixer.music.load(diretorio)
mixer.music.set_volume(0.3)
mixer.music.play(1)
print(f'>>> A música "{musica.title()}" foi iniciada.')
playlist.append(musica.title())


print(opcoes)


while True:
    opcao = str(input('\nQual sua opção: ')).strip()

# SAIR
    if opcao == '0':
        sair = comandos.sair()

        if sair == False:
            print(opcoes)

        if sair == True:
            print('>>> Programa finalizado!')
            exit()


# VOLUME
    elif opcao == '5':
        print(f'>>> O volume atual é {mixer.music.get_volume() * 10:.0f}.')


# MUDAR VOLUME
    elif opcao == '6':
        volume = str(input('\nDigite um novo volume: ')).strip()
        while not volume.isnumeric():
            print('>>> Digite apenas números.')
            volume = str(input('\nDigite um novo volume: ')).strip()
        while int(volume) not in range(11):
            print('>>> O volume suportado é de 0 a 10.')
            volume = str(input('\nDigite um novo volume: ')).strip()

        print(f'>>> O volume foi mudado de {mixer.music.get_volume() * 10:.0f} para {volume}.')
        mixer.music.set_volume(int(volume) / 10)


# PLAYLIST
    elif opcao == '8':
        cont = 1
        print('>>> As músicas reproduzidas foram:')
        for musica_tocadas in playlist:
            print(cont, '-', end=' ')
            print(musica_tocadas)
            cont += 1


# MUSICAS DISPONIVEIS
    elif opcao == '9':
        cont = 1
        print('>>> As músicas disponíveis são: ')

        diretorio_audio = path.dirname(path.realpath(__file__)) + '/audio'
        arquivo_lista_audio = listdir(diretorio_audio)

        for arquivo_lista in arquivo_lista_audio:
            print(cont, '-', end=' ')
            print(arquivo_lista[:-4])
            cont += 1


# VERIFICAR
    elif mixer.music.get_pos() == -1:
        print(f'>>> Não há nenhuma música tocando no momento.')

        acabou = str(input('Deseja ouvir mais uma música [sim/não]: ')).strip().lower()
        while acabou != 'sim' and acabou != 'não':
            print('>>> Digite uma opção válida.')
            acabou = str(input('\nDeseja ouvir mais uma música [sim/não]: ')).strip().lower()

        if acabou == 'não':
            break

        if acabou == 'sim':
            while True:
                musica = str(input('\nQual música deseja ouvir: ')).strip()
                while musica == '':
                    print('>>> Digite algo.')
                    print('>>> Lembre-se: apenas arquivos mp3 e são reproduzidos.')
                    musica = str(input('\nQual música deseja ouvir: ')).strip()

                if comandos.existe(musica) == True:
                    if comandos.ismp3(musica) ==  True:
                        arquivo = musica
                        musica = musica[:-4]
                        diretorio = comandos.diretorio(arquivo)
                        break
                    else:
                        arquivo = musica + '.mp3'
                        diretorio = comandos.diretorio(arquivo)
                        break

                if comandos.existe(musica) == False:
                    if comandos.ismp3(musica) == True:
                        print(f'>>> O arquivo "{musica}" não foi encontrado.')
                    else:
                        print(f'>>> A música "{musica}" não foi encontrada.')

            mixer.music.load(diretorio)
            mixer.music.set_volume(0.3)
            mixer.music.play(1)
            print(f'>>> A música "{musica.title()}" foi iniciada.')
            playlist.append(musica.title())

# SUBSTITUIR
    elif opcao == '1':
        musica_substituida = musica.title()

        while True:
                musica = str(input('\nQual música deseja ouvir: ')).strip()
                while musica == '':
                    print('>>> Digite algo.')
                    print('>>> Lembre-se: apenas arquivos mp3 são reproduzidos.')
                    musica = str(input('\nQual música deseja ouvir: ')).strip()

                if comandos.existe(musica) == True:
                    if comandos.ismp3(musica) ==  True:
                        arquivo = musica
                        musica = musica[:-4]
                        diretorio = comandos.diretorio(arquivo)
                        break
                    else:
                        arquivo = musica + '.mp3'
                        diretorio = comandos.diretorio(arquivo)
                        break

                if comandos.existe(musica) == False:
                    if comandos.ismp3(musica) == True:
                        print(f'>>> O arquivo "{musica}" não foi encontrado.')
                    else:
                        print(f'>>> A música "{musica}" não foi encontrada.')

        proseguir = str(input(f'Deseja substituir a música "{musica_substituida}" por "{musica}" '
                              f'[sim/não]: ')).strip().lower()
        while proseguir != 'sim' and proseguir != 'não':
            print('>>> Digite uma opção válida.')
            proseguir = str(input(f'Deseja substituir a música "{musica_substituida}" por "{musica}" '
                                  f'[sim/não]: ')).strip().lower()

        if proseguir == 'não':
            print(opcoes)

        if proseguir == 'sim':
            mixer.music.load(diretorio)
            mixer.music.play(1)
            print(f'>>> A música "{musica.title()}" foi iniciada, substituindo a música "{musica_substituida}".')
            playlist.append(musica.title())


# LOOP
    elif opcao == '2':
        print(opcoes_loop)

        opcao_loop = str(input('\nQual sua opção de looping: ')).strip()

        while True:
            while opcao_loop not in '1234':
                print('>>> Digite uma opção válida.')
                opcao_loop = str(input('\nQual sua opção de looping: ')).strip()

            # LOOP 1 VEZ
            if opcao_loop == '1':
                mixer.music.load(arquivo)
                mixer.music.play(1)
                print(f'>>> A música "{musica}" foi reiniciada e será tocada 1 vez.')
                print(opcoes)
                break

            # LOOP 3 VEZES
            elif opcao_loop == '2':
                mixer.music.load(arquivo)
                mixer.music.play(3)
                print(f'>>> A música "{musica}" foi reiniciada e será tocada 3 vezes.')
                print(opcoes)
                break

            # LOOP 4 VEZES
            elif opcao_loop == '3':
                mixer.music.load(arquivo)
                mixer.music.play(4)
                print(f'>>> A música "{musica}" foi reiniciada e será tocada 4 vezes.')
                print(opcoes)
                break

            # LOOP ATÉ REINICIAR
            if opcao_loop == '4':
                mixer.music.load(arquivo)
                mixer.music.play(-1)
                print(f'>>> A música "{musica}" foi reiniciada e será tocada até ser reiniciada novamente.')
                print(opcoes)
                break

            # LOOP ERRO
            else:
                print('>>> Digite uma opção válida.')


# REINICIAR
    elif opcao == '3':
        mixer.music.load(diretorio)
        mixer.music.play(1)
        mixer.music.rewind()
        print(f'>>> A música "{musica.title()}" foi reiniciada, juntamente com seus loops.')


# PAUSAR / DESPAUSAR
    elif opcao == '4':
        mixer.music.pause()
        print(f'>>> A música "{musica.title()}" foi pausada.')

        despausar = str(input('Pressione 4 novamente para despausar: '))
        while despausar != '4':
            print('>>> Apenas o número 4 pode ser digitado.')
            despausar = str(input('\nPressione 4 novamente para despausar: '))

        if despausar == '4':
            mixer.music.unpause()
            print(f'>>> A música "{musica.title()}" foi despausada.')


# NOME
    elif opcao == '7':
        print(f'>>> O nome da música atual é "{musica.title()}".')


# OPÇÃO INVÁLIDA
    else:
        print('>>> Digite uma opção válida.')
