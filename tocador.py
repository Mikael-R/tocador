from pygame import mixer
import comandos

playlist = list()
mixer.init()

while True:
    musica = str(input('\nQual música deseja ouvir: ')).strip()

    if comandos.existeArquivo(musica, 'audio') == True:
       arquivo = comandos.arquivoFormato(musica)
       musica = comandos.musicaFormato(musica)
       diretorio =  comandos.diretorioFormato('audio', arquivo)
       break
    else:
        print(comandos.inexisteArquivo(musica))

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
        else:
            print('>>> Programa finalizado!')
            exit()

# VOLUME
    elif opcao == '5':
        try:
            print(f'>>> O volume atual é {volume}.')
        except NameError:
            print(f'>>> O volume atual é 3.')

# MUDAR VOLUME
    elif opcao == '6':
        try:
            volume_anterior = volume
        except NameError:
            volume_anterior = 3
        volume = comandos.volume('Digite um novo volume: ')
        mixer.music.set_volume(volume / 10)
        print(f'>>> O volume foi mudado de {volume_anterior} para {volume}.')

# PLAYLIST
    elif opcao == '8':
        cont = 1
        print('>>> As músicas reproduzidas foram:')
        for musica_tocada in playlist:
            print(cont, '-', end=' ')
            print(musica_tocada)
            cont += 1

# MUSICAS DISPONÍVEIS
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
        acabou = comandos.acabou('Deseja ouvir mais uma música [sim/não]: ')

        if acabou == True:
            break
        else:
            while True:
                musica = str(input('\nQual música deseja ouvir: ')).strip()

                if comandos.existeArquivo(musica, 'audio') == True:
                    arquivo = comandos.arquivoFormato(musica)
                    musica = comandos.musicaFormato(musica)
                    diretorio =  comandos.diretorioFormato('audio', arquivo)
                    break
                else:
                    print(comandos.inexisteArquivo(musica))

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

                if comandos.existeArquivo(musica, 'audio') == True:
                    arquivo = comandos.arquivoFormato(musica)
                    musica = comandos.musicaFormato(musica)
                    diretorio =  comandos.diretorioFormato('audio', arquivo)
                    break
                else:
                    print(comandos.inexisteArquivo(musica))

        proseguir = comandos.prosseguir(f'Deseja substituir "{musica_substituida}" por "{musica}" [sim/não]: ')
        if proseguir == True:
            mixer.music.load(diretorio)
            mixer.music.play(1)
            print(f'>>> A música "{musica.title()}" foi iniciada, substituindo a música "{musica_substituida}".')
            playlist.append(musica.title())
        else:
            print(comandos.opcoes())

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

# NOME
    elif opcao == '7':
        print(f'>>> O nome da música atual é "{musica.title()}".')

# OPÇÃO INVÁLIDA
    else:
        print('>>> Digite uma opção válida.')
