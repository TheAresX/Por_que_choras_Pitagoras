import random
import pygame
from scripts.settings import *

from scripts.text import *

class Pergunta: #usa outras classe para receber texto e desenhar as perguntas dos desafios

    def __init__(self, text_ln1, text_ln2, text_ln3): #recebe texto da linha 1, 2 e 3
        self.display = pygame.display.get_surface()
        self.text_ln1 = text_ln1
        self.text_ln2 = text_ln2
        self.text_ln3 = text_ln3
        self.text_color = TEXT_COLOR
        self.text_position_ln1 = [116, 100]
        self.text_position_ln2 = [116, 145]
        self.text_position_ln3 = [116, 190]
        self.render_ln1 = Text(32, self.text_ln1, self.text_color, self.text_position_ln1)
        self.render_ln2 = Text(32, self.text_ln2, self.text_color, self.text_position_ln2)
        self.render_ln3 = Text(32, self.text_ln3, self.text_color, self.text_position_ln3)

    def draw(self): #desenha as 3 linhas de pergunta na tela
        self.render_ln1.drawFade()
        self.render_ln2.drawFade()
        self.render_ln3.drawFade()

class Opcoes: #constroe as opções na tela

    def __init__(self, text_op_correta, text_op_errada, text_op_errada2, funcao1, funcao2): #recebe texto da opcao correta e das duas opções errada, respectivamente, e funcao para opcao correta e funcao para opcoes erradas
        self.display = pygame.display.get_surface()
        self.fonte = pygame.font.Font(FONTE, 32)
        self.op_correta = text_op_correta
        self.op_errada = text_op_errada
        self.op_errada2 = text_op_errada2
        pos_y = [300, 370, 440]
        random.shuffle(pos_y) #sorteia aleatoreamente a posição no eixo y das opções
        self.position_op1 = pos_y[0]
        self.position_op2 = pos_y[1]
        self.position_op3 = pos_y[2]
        x = 180
        self.render_op1 = TextRect(32, self.op_correta,x, self.position_op1, funcao1)
        self.render_op2 = TextRect(32, self.op_errada,x, self.position_op2, funcao2)
        self.render_op3 = TextRect(32, self.op_errada2,x, self.position_op3, funcao2)

    def events(self, event): #recebe os eventos de clique e retorna a funcao para a classe TextRect
        self.render_op1.events(event)
        self.render_op2.events(event)
        self.render_op3.events(event)
    
    def draw(self): #desenha as opções na tela
        self.render_op1.draw()
        self.render_op2.draw()
        self.render_op3.draw()
        