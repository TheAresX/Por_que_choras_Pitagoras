import sys
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *

class GameOver(Scene): #constroe cena de game over ao final do jogo

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.music = pygame.mixer.music.load("assets/song/menu_backsound.mp3")
        pygame.mixer.music.play(-1)
        self.bg = AnimatedBg("assets/menu/bg.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        self.logo = Obj("assets/menu/gameover.png", [500,146], [self.all_sprites])
        self.btn_play = Button(PRIMARY_COLOR, 543, 438, 'Menu', SECONDARY_COLOR, self.next_scene)
        self.btn_quit = Button(PRIMARY_COLOR, 543, 530, 'Quit', SECONDARY_COLOR, self.quit_game)

    def next_scene(self): #funcao para retornar ao menu
        pygame.mixer.music.stop()
        self.active = False

    def quit_game(self): #funcao para fechar o programa
        pygame.quit()
        sys.exit()
    
    def events(self, event): #funcao para receber eventos do mouse
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False

        self.btn_play.events(event)
        self.btn_quit.events(event)

        return super().events(event)

    def update(self): #funcao para desenhar/atualizar objetos na tela
        self.bg.update()
        self.btn_play.draw()
        self.btn_quit.draw()
        return super().update()