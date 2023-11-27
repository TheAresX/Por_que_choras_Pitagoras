import random
import pygame
from scripts.settings import *

from scripts.text import *

class Pergunta:

    def __init__(self, text_ln1, text_ln2, text_ln3):
        self.display = pygame.display.get_surface()
        self.text_ln1 = text_ln1
        self.text_ln2 = text_ln2
        self.text_ln3 = text_ln3
        self.text_color = TEXT_COLOR
        self.text_position_ln1 = [170, 100]
        self.text_position_ln2 = [170, 135]
        self.text_position_ln3 = [170, 170]
        self.render_ln1 = Text(32, self.text_ln1, self.text_color, self.text_position_ln1)
        self.render_ln2 = Text(32, self.text_ln2, self.text_color, self.text_position_ln2)
        self.render_ln3 = Text(32, self.text_ln3, self.text_color, self.text_position_ln3)

    def draw(self):
        self.render_ln1.drawFade()
        self.render_ln2.drawFade()
        self.render_ln3.drawFade()

class Opcoes:

    def __init__(self, text_op_correta, text_op_errada, text_op_errada2):
        self.display = pygame.display.get_surface()
        self.fonte = pygame.font.Font(FONTE, 32)
        self.op_correta = text_op_correta
        self.op_errada = text_op_errada
        self.op_errada2 = text_op_errada2
        pos_y = [300, 370, 440]
        random.shuffle(pos_y)
        self.position_op1 = pos_y[0]
        self.position_op2 = pos_y[1]
        self.position_op3 = pos_y[2]
        x = 180
        self.render_op1 = TextRect(32, self.op_correta,x, self.position_op1)
        self.render_op2 = TextRect(32, self.op_errada,x, self.position_op2)
        self.render_op3 = TextRect(32, self.op_errada2,x, self.position_op3)

    def events(self, event):
        self.render_op1.events(event)
        self.render_op2.events(event)
        self.render_op3.events(event)
    
    def draw(self):
        self.render_op1.draw()
        self.render_op2.draw()
        self.render_op3.draw()