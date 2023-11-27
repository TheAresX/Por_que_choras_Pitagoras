import pygame

from scripts.settings import *


class Text: #classe que constroe texto de maneira genérica

    def __init__(self, size, text, color, pos): #recebe tamanho da fonte, string, cor e posicao

        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font(FONTE, size)
        self.text = self.font.render(text, True,color).convert_alpha()
        self.position = pos
        self.text_alpha = 0
        self.alpha_speed = 5
        self.color = color
        self.text_rect = self.text.get_rect(center=pos)

    def draw(self): #desenha o texto na tela
        self.display.blit(self.text, self.position)

    def draw_center(self): #desenha o texto centralizado em uma superficie (usado nos botoes)
        self.display.blit(self.text, self.text_rect)
    
    def update_text(self, text, color): #atualiza/desenha cor do texto
        self.text = self.font.render(text, True, color).convert_alpha()

    def drawFade(self): #desenha o texto com efeito surgir

        if self.text_alpha >= 0:
            self.text_alpha += self.alpha_speed
        else:
            self.text_alpha = 255

        self.text.set_alpha(self.text_alpha)
        self.display.blit(self.text, self.position)

class TextRect: #funcao para construir texto das opcoes
    def __init__(self, size, text, x, y, funcao): #recebe tamanho da fonte, string, posicao x, posicao y e funcao

        self.display = pygame.display.get_surface()
        self.color = (40,61,47)
        self.rect = pygame.Rect(x,y, 40, 48)
        self.text = text
        self.render = Text(size, self.text, TEXT_COLOR, [x,y])
        self.position = [x,y]
        self.funcao = funcao

    def events(self, event): #recebe as acoes do mouse
        if event.type == pygame.MOUSEMOTION: #muda a cor da opcao se o mouse estiver encima
            if self.rect.collidepoint(event.pos):
                self.render.update_text(self.text, (239,255,43))
            else: #retorna a cor da opcao se o mouse nao tiver encima
                self.render.update_text(self.text, TEXT_COLOR)
        if event.type == pygame.MOUSEBUTTONDOWN: #recebe a funcao quando a opcao é clicada
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.funcao()

    def draw(self): #desenha a opcao na tela
        pygame.draw.rect(self.display, self.color, self.rect)
        self.render.drawFade()