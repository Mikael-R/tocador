from pygame import mixer
import comandos

playlist = list()

mixer.init()

while True:
    musica = str(input('\nQual música deseja ouvir: ')).strip()
    while musica == '':
        print('>>> Digite algo.')
        print('>>> Lembre-se: apenas arquivos mp3 são reproduzidos.')
        musica = str(input('\nQual música deseja ouvir: ')).strip()

    if comandos.existeArquivo(musica, 'audio') == True:
        if comandos.ismp3(musica) ==  True:
            arquivo = musica
            musica = musica[:-4]
            diretorio = comandos.diretorio(arquivo)
            break
        else:
            arquivo = musica + '.mp3'
            diretorio = comandos.diretorio(arquivo)
            break

    if comandos.existeArquivo(musica, 'audio') == False:
        if comandos.ismp3(musica) == True:
            print(f'>>> O arquivo "{musica}" não foi encontrado.')
        else:
            print(f'>>> A música "{musica}" não foi encontrada.')

mixer.music.load(diretorio)
mixer.music.set_volume(0.3)
mixer.music.play(1)
print(f'>>> A música "{musica.title()}" foi iniciada.')
playlist.append(musica.title())


print(comandos.opcoes())


while True:
    opcao = str(input('\nQual sua opção: ')).strip()

# SAIR
    if opcao == '0':
        sair = comandos.sair('Deseja sair do programa [sim/não]: ')

        if sair == False:
            print(comandos.opcoes())

        if sair == True:
            print('>>> Programa finalizado!')
            exit()


# VOLUME
    elif opcao == '5':
        print(f'>>> O volume atual é {mixer.music.get_volume() * 10:.0f}.')


# MUDAR VOLUME
    elif opcao == '6':
        volume = comandos.volume('Digite um novo volume: ')

        print(f'>>> O volume foi mudado de {mixer.music.get_volume() * 10:.0f} para {volume}.')
        mixer.music.set_volume(volume / 10)


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

        if comandos.existeDiretorio('audio'):
            print('>>> As músicas disponíveis são: ')
            lista_musicas = comandos.disponiveis('audio')
            cont = 1

            for lista_musica in lista_musicas:
                print(cont, '-', end=' ')
                print(lista_musica[:-4])
                cont += 1
        else:
            print('>>> Diretorio de músicas não encontrado.')


# VERIFICAR
    elif mixer.music.get_pos() == -1:
        print(f'>>> Nenhuma música tocando no momento.')

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

                if comandos.existeArquivo(musica, 'audio') == True:
                    if comandos.ismp3(musica) ==  True:
                        arquivo = musica
                        musica = musica[:-4]
                        diretorio = comandos.diretorio(arquivo)
                        break
                    else:
                        arquivo = musica + '.mp3'
                        diretorio = comandos.diretorio(arquivo)
                        break

                if comandos.existeArquivo(musica, 'audio') == False:
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

                if comandos.existeArquivo(musica, 'audio') == True:
                    if comandos.ismp3(musica) ==  True:
                        arquivo = musica
                        musica = musica[:-4]
                        diretorio = comandos.diretorio(arquivo)
                        break
                    else:
                        arquivo = musica + '.mp3'
                        diretorio = comandos.diretorio(arquivo)
                        break

                if comandos.existeArquivo(musica, 'audio') == False:
                    if comandos.ismp3(musica) == True:
                        print(f'>>> O arquivo "{musica}" não foi encontrado.')
                    else:
                        print(f'>>> A música "{musica}" não foi encontrada.')

        proseguir = str(input(f'Deseja substituir "{musica_substituida}" por "{musica}" [sim/não]: ')).strip().lower()
        while proseguir != 'sim' and proseguir != 'não':
            print('>>> Digite uma opção válida.')
            proseguir = str(input(f'Deseja substituir "{musica_substituida}" por "{musica}" [sim/não]: ')).strip().lower()

        if proseguir == 'não':
            print(comandos.opcoes())

        if proseguir == 'sim':
            mixer.music.load(diretorio)
            mixer.music.play(1)
            print(f'>>> A música "{musica.title()}" foi iniciada, substituindo a música "{musica_substituida}".')
            playlist.append(musica.title())


# LOOP
    elif opcao == '2':
        print(comandos.opcoes_loop())

        while True:
            opcao_loop = str(input('\nQual sua opção: ')).strip()

            # LOOP 1 VEZ
            if opcao_loop == '1':
                mixer.music.play(1)
                print(f'>>> A música "{musica}" foi reiniciada e será tocada 1 vez.')
                print(comandos.opcoes())
                break

            # LOOP 3 VEZES
            elif opcao_loop == '2':
                mixer.music.play(3)
                print(f'>>> A música "{musica}" foi reiniciada e será tocada 3 vezes.')
                print(comandos.opcoes())
                break

            # LOOP 4 VEZES
            elif opcao_loop == '3':
                mixer.music.play(4)
                print(f'>>> A música "{musica}" foi reiniciada e será tocada 4 vezes.')
                print(comandos.opcoes())
                break

            # LOOP ATÉ REINICIAR
            if opcao_loop == '4':
                mixer.music.play(-1)
                print(f'>>> A música "{musica}" foi reiniciada e será tocada até ser reiniciada novamente.')
                print(comandos.opcoes())
                break

            # LOOP ERRO
            else:
                print('>>> Digite uma opção válida.')


# REINICIAR
    elif opcao == '3':
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
