import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 1900
altura = 1000
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Forca')

# Cores
BRANCO = (255, 255, 255)
PRETO = (50, 0, 25)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Fontes
fonte_grande = pygame.font.Font(None, 80)
fonte_pequena = pygame.font.Font(None, 36)

def tela_inicial():
    # Loop da tela inicial
    while True:
        janela.fill(PRETO)
        
        # Texto de Loading
        texto_loading = fonte_grande.render('Trabalho De Redes', True, BRANCO)
        texto_rect = texto_loading.get_rect(center=(largura // 2, altura // 2 - 50))
        janela.blit(texto_loading, texto_rect)
        
        # Botões: Play e Créditos
        botao_play = pygame.Rect(largura // 2 - 50, altura // 2 + 20, 100, 50)
        pygame.draw.rect(janela, VERDE, botao_play)
        texto_play = fonte_pequena.render('Play', True, BRANCO)
        texto_play_rect = texto_play.get_rect(center=botao_play.center)
        janela.blit(texto_play, texto_play_rect)
        
        botao_creditos = pygame.Rect(largura // 2 - 50, altura // 2 + 90, 100, 50)
        pygame.draw.rect(janela, AZUL, botao_creditos)
        texto_creditos = fonte_pequena.render('Créditos', True, BRANCO)
        texto_creditos_rect = texto_creditos.get_rect(center=botao_creditos.center)
        janela.blit(texto_creditos, texto_creditos_rect)
        
        # Atualizar a tela
        pygame.display.flip()
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Verificar clique nos botões
                pos_mouse = pygame.mouse.get_pos()
                if botao_play.collidepoint(pos_mouse):
                    return 'play'
                elif botao_creditos.collidepoint(pos_mouse):
                    mostrar_creditos()
        
        # Limitar a taxa de atualização da tela
        pygame.time.Clock().tick(30)

def mostrar_creditos():
    # Tela de créditos
    creditos = True
    while creditos:
        janela.fill(PRETO)
        
        # Texto de créditos
        texto_cred = fonte_pequena.render('Desenvolvido por: Amanda, Caio e Danilo', True, BRANCO)
        texto_rect = texto_cred.get_rect(center=(largura // 2, altura // 2))
        janela.blit(texto_cred, texto_rect)
        
        # Botão de sair dos créditos
        botao_sair = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(janela, VERMELHO, botao_sair)
        texto_sair = fonte_pequena.render('Sair', True, BRANCO)
        texto_sair_rect = texto_sair.get_rect(center=botao_sair.center)
        janela.blit(texto_sair, texto_sair_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos_mouse = pygame.mouse.get_pos()
                if botao_sair.collidepoint(pos_mouse):
                    creditos = False
        
        pygame.time.Clock().tick(30)

def jogar_forca():
    while True:
        palavra = escolher_palavra()
        letras_certas = []
        letras_erradas = []
        tentativas = 6
        
        while True:
            janela.fill(PRETO)
            
            # Desenhar palavra oculta
            palavra_oculta = ''
            for letra in palavra:
                if letra in letras_certas:
                    palavra_oculta += letra + ' '
                else:
                    palavra_oculta += '_ '
            texto_palavra = fonte_grande.render(palavra_oculta, True, BRANCO)
            janela.blit(texto_palavra, (100, 100))
            
            # Desenhar letras erradas
            texto_erradas = fonte_pequena.render(f'Letras erradas: {" ".join(letras_erradas)}', True, BRANCO)
            janela.blit(texto_erradas, (100, 250))
            
            # Desenhar tentativas restantes
            texto_tentativas = fonte_pequena.render(f'Tentativas restantes: {tentativas}', True, BRANCO)
            janela.blit(texto_tentativas, (100, 300))
            
            # Atualizar a tela
            pygame.display.flip()
            
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pausado = True
                        while pausado:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        pausado = False
                            pygame.time.Clock().tick(30)
            
            # Lógica do jogo da forca
            if all(letra in letras_certas for letra in palavra):
                mostrar_mensagem('Parabéns! Você venceu!')
                break
            elif tentativas == 0:
                mostrar_mensagem(f'Você perdeu! A palavra era {palavra}')
                break
            
            # Capturar entrada do jogador
            letra = capturar_letra()
            
            # Verificar se a letra está na palavra
            if letra in palavra:
                letras_certas.append(letra)
            else:
                letras_erradas.append(letra)
                tentativas -= 1
        
        # Perguntar se deseja jogar novamente
        if not jogar_novamente():
            break

def escolher_palavra():
    # Lista expandida de palavras relacionadas a animais
    palavras = [
        'GATO', 'CACHORRO', 'ELEFANTE', 'GIRAFA', 'LEÃO', 'TIGRE', 'GOLFINHO', 'PANDA', 'BALEIA',
        'MACACO', 'GALINHA', 'PINGUIM', 'PAPAGAIO', 'CROCODILO', 'HIPOPÓTAMO', 'RINOCERONTE',
        'SURICATO', 'MORCEGO', 'COALA', 'JACARÉ', 'POLVO', 'SERPENTE', 'PANTERA', 'URSO',
        'RATO', 'ORANGOTANGO', 'FOCA', 'LOBO', 'CORUJA', 'ABELHA', 'CAVALO', 'FORMIGA',
        'CARANGUEJO', 'ESCORPIÃO', 'TARTARUGA', 'ALBATROZ', 'CORDEIRO', 'DONINHA', 'GAMBÁ'
    ]
    return random.choice(palavras)

def capturar_letra():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    return chr(event.key).upper()

def mostrar_mensagem(mensagem):
    # Mostra uma mensagem na tela por alguns segundos
    texto = fonte_pequena.render(mensagem, True, BRANCO)
    texto_rect = texto.get_rect(center=(largura // 2, altura // 2))
    janela.blit(texto, texto_rect)
    pygame.display.flip()
    pygame.time.delay(2000)  # Delay de 2 segundos

def jogar_novamente():
    texto_replay = fonte_pequena.render('Deseja jogar novamente? (S/N)', True, BRANCO)
    texto_replay_rect = texto_replay.get_rect(center=(largura // 2, altura // 2 + 50))
    janela.blit(texto_replay, texto_replay_rect)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return True
                elif event.key == pygame.K_n:
                    return False

if __name__ == '__main__':
    print('Bem-vindo ao Jogo da Forca!')
    
    # Tela inicial
    opcao = tela_inicial()
    
    if opcao == 'play':
        print('Iniciando jogo...')
        jogar_forca()
    
    print('Obrigado por jogar!')
    pygame.quit()
