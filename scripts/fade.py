import pygame
from scripts.settings import *

class Fade: #dá o esfeito de esmanecimento(sugir) as funções de desenho de outras classe

    def __init__(self, speed): #recebe velocidade do surgimento
        
        self.display = pygame.display.get_surface()
        self.surface = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.surface.fill("black")

        self.alpha = 255
        self.speed = speed
    
    def draw(self): #desenha o objeto com o efeito de surgir

        if self.alpha > 0:
            self.alpha -= self.speed

        self.surface.set_alpha(self.alpha)
        self.display.blit(self.surface, [0,0])