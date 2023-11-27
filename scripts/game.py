import pygame
from scripts.animatedbg import AnimatedBg
from scripts.construtor import *
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *

#o script constroes todas as cenas do game (apresentacao, introducoes e desafios)
#acertou: realiza funcoes para resposta correta
#errou: realiza funcoes para responsta errada
#events: recebe as interacoes do mouse
#draw: desenha na tela
#update: atualiza os desenhos na tela

class Apresentacao(Scene): 

    def __init__(self):
        super().__init__()

        self.music = pygame.mixer.music.load('assets/song/backsound.mp3')
        pygame.mixer.music.play(-1)
        self.bg = AnimatedBg('assets/level/bg.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/professor_dev.png', [0,0], [self.all_sprites])
        Obj('assets/level/apre_dev.png', [128, 105], [self.all_sprites] )

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.active = False
        return super().events(event)
                
    def update(self):
        self.bg.update()
        return super().update()
    
class Intro(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg('assets/level/bg.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/professor_dev.png', [0,0], [self.all_sprites])
        Obj('assets/level/intro01.png', [128, 105], [self.all_sprites] )

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.active = False
        return super().events(event)
                
    def update(self):
        self.bg.update()
        return super().update()

class Fase01_0(Scene):

    def __init__(self):
        super().__init__()

        self.fase = FASE1
        self.index = 0
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])

    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_1(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 1
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])

    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_2(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 2
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_3(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 3
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])

    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_4(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 4
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])      
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_5(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 5
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])   
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_6(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 6
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])     
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_7(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 7
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_8(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 8
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase01_9(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE1
        self.index = 9
        self.bg = AnimatedBg("assets/level/bg_brawl.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Intro2_1(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.bg = AnimatedBg('assets/level/bg.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/professor_dev.png', [0,0], [self.all_sprites])
        Obj('assets/level/intro02.png', [100, 105], [self.all_sprites] )

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.active = False
        return super().events(event)
                
    def update(self):
        self.bg.update()
        return super().update()
    
class Fase02_0(Scene):

    def __init__(self):
        super().__init__()

        self.fase = FASE2
        self.index = 0
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase02_1(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 1
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase02_2(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 2
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase02_3(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 3
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase02_4(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 4
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase02_5(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 5
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase02_6(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 6
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase02_7(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 7
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase02_8(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 8
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase02_9(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE2
        self.index = 9
        self.bg = AnimatedBg("assets/level/bg_clash.png", [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Intro3_1(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.bg = AnimatedBg('assets/level/bg.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/professor_dev.png', [0,0], [self.all_sprites])
        Obj('assets/level/intro03.png', [128, 105], [self.all_sprites] )

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.active = False
        return super().events(event)
                
    def update(self):
        self.bg.update()
        return super().update()
    
class Fase03_0(Scene):

    def __init__(self):
        super().__init__()

        self.fase = FASE3
        self.index = 0
        self.bg = AnimatedBg('assets/level/bg_mario.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase03_1(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE3
        self.index = 1
        self.bg = AnimatedBg('assets/level/bg_mario.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase03_2(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE3
        self.index = 2
        self.bg = AnimatedBg('assets/level/bg_mario.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()
    
class Fase03_3(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE3
        self.index = 3
        self.bg = AnimatedBg('assets/level/bg_mario.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        self.active = False

    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()

class Fase03_4(Scene):

    def __init__(self):
        super().__init__()

        pygame.time.Clock().tick(1)
        self.fase = FASE3
        self.index = 4
        self.bg = AnimatedBg('assets/level/bg_mario.png', [0,0], [0, -HEIGHT], [self.all_sprites])
        Obj('assets/level/quadro.png', [45,45], [self.all_sprites])
        self.pergunta = Pergunta(self.fase[f'pergunta{self.index}'][0], self.fase[f'pergunta{self.index}'][1], self.fase[f'pergunta{self.index}'][2])
        self.opcoes = Opcoes(self.fase[f'certa{self.index}'], self.fase[f'errada{self.index}'][0], self.fase[f'errada{self.index}'][1], self.acertou, self.errou)
        Obj(self.fase[f'img{self.index}'][0], self.fase[f'img{self.index}'][1], [self.all_sprites])  
    
    def acertou(self):
        self.music = pygame.mixer.Sound("assets/song/confirm.wav")
        self.music.play()
        Obj('assets/level/acertou.png', [499, 272], [self.all_sprites])
        pygame.mixer.music.stop()
        self.active = False
    
    def errou(self):
        self.music = pygame.mixer.Sound("assets/song/fail.wav")
        self.music.play()
        Obj('assets/level/errou.png', [499, 272], [self.all_sprites])
        pygame.mixer.music.stop()
        self.active = False
        
    def events(self, event):
        self.opcoes.events(event)
        return super().events(event)
                
    def update(self):
        self.bg.update()
        self.pergunta.draw()
        self.opcoes.draw()
        return super().update()