import sys
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *

class Menu(Scene): #constroe o menu na tela

    def __init__(self):
        super().__init__()

        self.music = pygame.mixer.music.load("assets/song/menu_backsound.mp3") #diretorio musica de menu
        pygame.mixer.music.play(-1) #inicia musica de menu

        self.bg = AnimatedBg("assets/menu/bg.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        self.logo = Obj("assets/menu/logo.png", [278,134], [self.all_sprites])
        self.btn_play = Button(PRIMARY_COLOR, 543, 438, 'Play', SECONDARY_COLOR, self.next_scene)
        self.btn_quit = Button(PRIMARY_COLOR, 543, 530, 'Quit', SECONDARY_COLOR, self.quit_game)

    def next_scene(self): #funcao para iniciar o game
        pygame.mixer.music.stop() #encerra musica de menu
        self.active = False

    def quit_game(self): #funcao para encerrar o programa
        pygame.quit()
        sys.exit()
    
    def events(self, event): #recebe as interacoes do mouse
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False

        self.btn_play.events(event)
        self.btn_quit.events(event)

        return super().events(event)

    def update(self): #atualiza/desenha os objetos na tela
        self.bg.update()
        self.btn_play.draw()
        self.btn_quit.draw()
        return super().update()




