from scripts.obj import Obj
from scripts.settings import HEIGHT

class AnimatedBg: #classe para construir e desenhar os fundos animados na tela

    def __init__(self, img, pos1,pos2, group): #recebe caminho da imagem, posicao e grupo onde ficará armazenada
        self.bg = Obj(img,pos1, group)
        self.bg2 = Obj(img,pos2, group)
    
    def update(self): #atualiza o backgroud, dando a percepção de movimento

        self.bg.rect.y += 1
        self.bg2.rect.y += 1

        if self.bg.rect.y > HEIGHT:
            self.bg.rect.y = 0
        elif self.bg2.rect.y == 0:
            self.bg2.rect.y = -HEIGHT