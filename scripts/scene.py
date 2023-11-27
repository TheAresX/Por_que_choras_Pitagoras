import pygame
from scripts.fade import Fade
from scripts.settings import *

class Scene: #classe generica para contruir as cenas de apresentacao, introducao e fases do game

    def __init__(self):
        
        self.display = pygame.display.get_surface() #recebe tela
        self.all_sprites = pygame.sprite.Group() #grupo que armazena objetos das cenas
        self.active = True

        self.fade = Fade(15) #controle do efeito surgir

    def events(self, event):
        pass

    def draw(self): #funcao generica para desenhar objetos na tela
        self.all_sprites.draw(self.display)

    def update(self): #funcao generica para atualizar/desenhar objetos na tela
        self.fade.draw()
        self.all_sprites.update()







