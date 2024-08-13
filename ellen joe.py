## ELLEN JOE + BEEPER FUNK
import pygame
from pygame.locals import *
from sys import exit
import os
import glob

pygame.init()

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Toda Princesa - by:(LuizQJ)")

pygame.mixer.init()
musica_braba = pygame.mixer.music.load("musicateste.mp3")
pygame.mixer.music.play(-1)
volume = pygame.mixer.music.set_volume(0.3)

## ellen = pygame.image.load(os.path.join("ellen-joe.gif"))
## cordenada = ellen.get_rect(center=(320,250))

dance = "ellen-dance" #VARIAVEL RECEBE A PASTA
padrao_nome = os.path.join(dance, "frame_*.gif") #DEFINIR UM PADRAO AOS ARQUIVOS DA PASTA
sprites = [] # LISTA ONDE VAI FICAR AS IMAGENS
frame = 0

arquivo = glob.glob(padrao_nome)
arquivo.sort()

for caminho in arquivo:
    image = pygame.image.load(caminho).convert_alpha()
    sprites.append(image)

## LOOP PARA O PROGRAMA CONTINUAR RODANDO
while True:
    for event in pygame.event.get(): # IDENTIFICA O EVENTO
        if event.type == QUIT:  # SE O EVENTO FOR "SAIR, O PROGRAMA ENCERRRA"
            pygame.quit()
            exit()

        
    tela.blit(sprites[frame], (75,10))
    frame = (frame + 1) % len(sprites)  
    pygame.display.flip()
    pygame.time.delay(25)
    

