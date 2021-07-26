import sys
import pygame
from settings import Settings #импортируем настройки из settings.py


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.stgs = Settings()# используем класс с настройками
        #self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode((self.stgs.scr_wh, self.stgs.scr_ht))

        pygame.display.set_caption("Alien Invasion")
        #self.bg_color = (230, 230,230) #меняем цвет фона
        self.bg_color = self.stgs.bg_cr

    def run_game(self):
        """Основной цикл игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)#заполняем экран цветом фона
            #отображение последнего прорисованного экрана
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
