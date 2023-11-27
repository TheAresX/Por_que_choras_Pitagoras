import pygame, sys
from scripts.menu import Menu
from scripts.game import *
from scripts.gameover import GameOver
from scripts.settings import *

class StartGame: #classe que controla as cenas

    def __init__(self):

        pygame.init() #inicia a biblioteca pygame
        pygame.mixer.init() #inicia o mixer de sons do pygame
        pygame.font.init() #inicia as funções destinadas a contrucao de texto
        pygame.display.set_caption("Por que Choras, Pitágoras?") #altera o título da janela
        
        self.display = pygame.display.set_mode([WIDTH,HEIGHT]) #constre a janela
        self.scene = "menu" #controle de cena
        self.current_scene = Menu() #classe da cena inicial

        self.fps = pygame.time.Clock() #funcao para controlar FPS da tela
    
    def run(self):
        
        while True:

            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "apresentacao"
                self.current_scene = Apresentacao()
            
            elif self.scene == "apresentacao" and self.current_scene.active == False:
                self.scene = "intro01"
                self.current_scene = Intro()
            elif self.scene == "intro01" and self.current_scene.active == False:
                self.scene = "fase01_0"
                self.current_scene = Fase01_0()
            elif self.scene == "fase01_0" and self.current_scene.active == False:
                self.scene = "fase01_1"
                self.current_scene = Fase01_1()
            elif self.scene == "fase01_1" and self.current_scene.active == False:
                self.scene = "fase01_2"
                self.current_scene = Fase01_2()
            elif self.scene == "fase01_2" and self.current_scene.active == False:
                self.scene = "fase01_3"
                self.current_scene = Fase01_3()
            elif self.scene == "fase01_3" and self.current_scene.active == False:
                self.scene = "fase01_4"
                self.current_scene = Fase01_4()
            elif self.scene == "fase01_4" and self.current_scene.active == False:
                self.scene = "fase01_5"
                self.current_scene = Fase01_5()
            elif self.scene == "fase01_5" and self.current_scene.active == False:
                self.scene = "fase01_6"
                self.current_scene = Fase01_6()
            elif self.scene == "fase01_6" and self.current_scene.active == False:
                self.scene = "fase01_7"
                self.current_scene = Fase01_7()
            elif self.scene == "fase01_7" and self.current_scene.active == False:
                self.scene = "fase01_8"
                self.current_scene = Fase01_8()
            elif self.scene == "fase01_8" and self.current_scene.active == False:
                self.scene = "fase01_9"
                self.current_scene = Fase01_9()
            
            elif self.scene == "fase01_9" and self.current_scene.active == False:
                self.scene = "intro2_1"
                self.current_scene = Intro2_1()
            elif self.scene == "intro2_1" and self.current_scene.active == False:
                self.scene = "fase02_0"
                self.current_scene = Fase02_0()
            elif self.scene == "fase02_0" and self.current_scene.active == False:
                self.scene = "fase02_1"
                self.current_scene = Fase02_1()
            elif self.scene == "fase02_1" and self.current_scene.active == False:
                self.scene = "fase02_2"
                self.current_scene = Fase02_2()
            elif self.scene == "fase02_2" and self.current_scene.active == False:
                self.scene = "fase02_3"
                self.current_scene = Fase02_3()
            elif self.scene == "fase02_3" and self.current_scene.active == False:
                self.scene = "fase02_4"
                self.current_scene = Fase02_4()
            elif self.scene == "fase02_4" and self.current_scene.active == False:
                self.scene = "fase02_5"
                self.current_scene = Fase02_5()
            elif self.scene == "fase02_5" and self.current_scene.active == False:
                self.scene = "fase02_6"
                self.current_scene = Fase02_6()
            elif self.scene == "fase02_6" and self.current_scene.active == False:
                self.scene = "fase02_7"
                self.current_scene = Fase02_7()
            elif self.scene == "fase02_7" and self.current_scene.active == False:
                self.scene = "fase02_8"
                self.current_scene = Fase02_8()
            elif self.scene == "fase02_8" and self.current_scene.active == False:
                self.scene = "fase02_9"
                self.current_scene = Fase02_9()

            elif self.scene == "fase02_9" and self.current_scene.active == False:
                self.scene = "intro3_1"
                self.current_scene = Intro3_1()
            elif self.scene == "intro3_1" and self.current_scene.active == False:
                self.scene = "fase03_0"
                self.current_scene = Fase03_0()
            elif self.scene == "fase03_0" and self.current_scene.active == False:
                self.scene = "fase03_1"
                self.current_scene = Fase03_1()
            elif self.scene == "fase03_1" and self.current_scene.active == False:
                self.scene = "fase03_2"
                self.current_scene = Fase03_2()
            elif self.scene == "fase03_2" and self.current_scene.active == False:
                self.scene = "fase03_3"
                self.current_scene = Fase03_3()
            elif self.scene == "fase03_3" and self.current_scene.active == False:
                self.scene = "fase03_4"
                self.current_scene = Fase03_4()

            elif self.scene == "fase03_4" and self.current_scene.active == False:
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get(): #funcao para receber eventos (interacoes)
                if event.type == pygame.QUIT: #evento de fechar o programa
                    pygame.quit()
                    sys.exit()
                self.current_scene.events(event)
            
            self.fps.tick(60) #controle do FPS
            self.display.fill("black") #fundo preto da janela
            self.current_scene.draw() #desenha a cena atual
            self.current_scene.update() #atualiza a cena atual
            pygame.display.flip() #atualiza a janela