import pygame
from scripts.settings import *

from scripts.text import Text

#classe que constroe os botões interativos com as funções de movimento e clique do mouse
class Button:

    def __init__(self, color, x, y, text, text_color, funcao): #recebe cor, posicao x, posicao y, string, cor do texto e funcao
        self.display = pygame.display.get_surface()
        self.color = color
        self.rect = pygame.Rect(x, y, 196,69)
        self.text = text
        self.text_color = text_color
        self.text_position = [x + self.rect.width/2, y + self.rect.height/2]
        self.render = Text(40, self.text, self.text_color, self.text_position)
        self.funcao = funcao

    def events(self, event):
        if event.type == pygame.MOUSEMOTION: #identifica o movimento do mouse e muda a cor dos botões e das letras
            if self.rect.collidepoint(event.pos):
                self.color = SECONDARY_COLOR
                self.render.update_text(self.text, PRIMARY_COLOR)
            else:
                self.color = PRIMARY_COLOR
                self.render.update_text(self.text, SECONDARY_COLOR)
        
        if event.type == pygame.MOUSEBUTTONDOWN: #rebece a ação de clique do mouse e realiza uma função
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.funcao()

    def draw(self): #desenha o botão na tela
        pygame.draw.rect(self.display, self.color, self.rect)
        self.render.draw_center()