import pygame

class Obj(pygame.sprite.Sprite): #classe genérica para construir objetos das imagens

    def __init__(self,img,pos, *groups): #recebe diretorio de imagem, posicao e grupo em que o objeto ficará armazenado
        super().__init__(*groups)

        self.display = pygame.display.get_surface()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = pos)

        self.posicao = pos
    
    def draw(self): #desenha os objetos na tela
        self.display.blit(self.image, self.posicao)

