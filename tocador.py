from pygame import mixer
import comandos

playlist = list()
mixer.init()
comandos.limpar()

while True:
    musica = str(input('\nQual música deseja ouvir: ')).strip()
    if comandos.musicaExiste(musica):
        if comandos.musicaDuplicada(musica):
            print(f'>>> A música "{musica.title()}" foi encontrada com outro(s) formato(s) no mesmo diretório, especifique um formato.')
        else:
            arquivo   = comandos.arquivoFormatado(musica)
            musica    = comandos.musicaFormatada(musica)
            diretorio = comandos.diretorioFormatado(arquivo)
            break
    else:
        print(comandos.musicaInexiste(musica))

mixer.music.load(diretorio)
mixer.music.set_volume(0.3)
mixer.music.play(1)
print(f'>>> A música "{musica.title()}" foi iniciada.')
playlist.append(musica.title())

print(comandos.opcoes())

while True:
    opcao = str(input('\nQual sua opção: ')).strip()

# SAIR #
    if opcao == '0':
        sair = comandos.sair('Deseja sair do programa [sim/não]: ')
        if sair == False:
            print(comandos.opcoes())
        else:
            print('>>> Programa finalizado!')
            exit()

# VOLUME #
    elif opcao == '2':
        try:
            print(f'>>> O volume atual é {volume}.')
        except NameError:
            print(f'>>> O volume atual é 3.')

# ALTERAR VOLUME #
    elif opcao == '3':
        try:
            volume_anterior = volume
        except NameError:
            volume_anterior = 3
        volume = comandos.volume('Digite um novo volume: ')
        mixer.music.set_volume(volume / 10)
        print(f'>>> O volume foi mudado de {volume_anterior} para {volume}.')

# MÚSICAS DISPONÍVEIS #
    elif opcao == '4':
        lista_musicas = comandos.musicasDisponiveis()
        if lista_musicas != 'NONE':
            print('>>> As músicas disponíveis são: ')
            cont = 1
            for lista_musica in lista_musicas:
                print(cont, '-', end=' ')
                print(lista_musica[:-4])
                cont += 1
        else:
            print('>>> O diretório das músicas não foi encontrado.')

# MÚSICAS REPRODUZIDAS #
    elif opcao == '5':
        cont = 1
        print('>>> As músicas reproduzidas foram:')
        for musica_tocada in playlist:
            print(cont, '-', end=' ')
            print(musica_tocada)
            cont += 1

# VERIFICAR #
    elif comandos.musicaTocando() == False:
        print(f'>>> Nenhuma música tocando no momento.')
        acabou = comandos.acabou('Deseja ouvir mais uma música [sim/não]: ')
        if acabou == True:
            break
        else:
            while True:
                musica = str(input('\nQual música deseja ouvir: ')).strip()
                if comandos.musicaExiste(musica):
                    if comandos.musicaDuplicada(musica):
                        print(f'>>> A música "{musica.title()}" foi encontrada com outro(s) formato(s) no mesmo diretório, especifique um formato.')
                    arquivo   = comandos.arquivoFormatado(musica)
                    musica    = comandos.musicaFormatada(musica)
                    diretorio = comandos.diretorioFormatado(arquivo)
                    break
                else:
                    print(comandos.musicaInexiste(musica))

            mixer.music.load(diretorio)
            mixer.music.play(1)
            print(f'>>> A música "{musica.title()}" foi iniciada.')
            playlist.append(musica.title())

# SUBSTITUIR #
    elif opcao == '1':
        musica_substituida = musica.title()

        while True:
                musica = str(input('\nQual música deseja ouvir: ')).strip()
                if comandos.musicaExiste(musica):
                    if comandos.musicaDuplicada(musica):
                        print(f'>>> A música "{musica.title()}" foi encontrada com outro(s) formato(s) no mesmo diretório, especifique um formato.')
                    arquivo   = comandos.arquivoFormatado(musica)
                    musica    = comandos.musicaFormatada(musica)
                    diretorio = comandos.diretorioFormatado(arquivo)
                    break
                else:
                    print(comandos.musicaInexiste(musica))

        proseguir = comandos.prosseguir(f'Deseja substituir "{musica_substituida}" por "{musica.title()}" [sim/não]: ')
        if proseguir == True:
            mixer.music.load(diretorio)
            mixer.music.play(1)
            print(f'>>> A música "{musica.title()}" foi iniciada, substituindo a música "{musica_substituida}".')
            playlist.append(musica.title())
        else:
            print(comandos.opcoes())

# LOOP #
    elif opcao == '6':
        print(comandos.opcoesLoop())

        while True:
            opcao_loop = str(input('\nQual sua opção: ')).strip()

            # LOOP 3 VEZES #
            if opcao_loop == '1':
                loop = 3
                break
            # LOOP 4 VEZES #
            elif opcao_loop == '2':
                loop = 4
                break
            # LOOP ATÉ REINICIAR #
            if opcao_loop == '3':
                loop = -1
                break
            # LOOP ERRO #
            else:
                print('>>> Digite uma opção válida.')

        mixer.music.play(loop)
        if loop == -1:
            print(f'>>> A música "{musica}" foi reiniciada e será tocada até ser reiniciada novamente.')
        else:
            print(f'>>> A música "{musica}" foi reiniciada e será tocada {loop} vezes.')


# REINICIAR #
    elif opcao == '7':
        mixer.music.play(1)
        mixer.music.rewind()
        print(f'>>> A música "{musica}" foi reiniciada, com seus loops retirados.')


# PAUSAR / DESPAUSAR #
    elif opcao == '8':
        try:
            if pause == True:
                mixer.music.unpause()
                pause = False
                print(f'>>> A música "{musica.title()}" foi despausada.')
            else:
                pause = True
                mixer.music.pause()
                print(f'>>> A música "{musica.title()}" foi pausada.')
        except NameError:
            pause = True
            mixer.music.pause()
            print(f'>>> A música "{musica.title()}" foi pausada.')

# OPÇÃO INVÁLIDA #
    else:
        print('>>> Digite uma opção válida.')
