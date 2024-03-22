import pygame
import sys

class Menu:
    """
    Hlavni menu hry, hrac si zde vybere, zda spusti hru, instrukce, nebo opusti hru
    """
    def __init__(self, screen, background_image, custom_font):
        """
        inicializace menu s pozadim a fontem
        """
        self.screen = screen
        self.background_image = background_image
        self.custom_font = custom_font
        self.current_button = 0

    def run(self):
        """
        Spousti hlavni cyklus
        """
        
        WHITE = (255, 255, 255)  # definujeme si barvy
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)

        buttons = [("Play", WHITE), ("Help", WHITE), ("Exit", WHITE)]

        while True:
            mx, my = pygame.mouse.get_pos()

            self.screen.blit(self.background_image, (0, 0))

            play_button = pygame.Rect(300, 200, 200, 0)  # vykreslovani tlacitek
            help_button = pygame.Rect(300, 300, 200, 0)
            exit_button = pygame.Rect(300, 400, 200, 0)

            pygame.draw.rect(self.screen, BLACK, play_button)
            self.draw_text(buttons[0][0], self.custom_font, buttons[0][1], 400, 225)

            pygame.draw.rect(self.screen, BLACK, help_button)
            self.draw_text(buttons[1][0], self.custom_font, buttons[1][1], 400, 325)

            pygame.draw.rect(self.screen, BLACK, exit_button)
            self.draw_text(buttons[2][0], self.custom_font, buttons[2][1], 400, 425)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # pohyb mezi tlacitky
                    if event.key == pygame.K_DOWN:
                        self.current_button = (self.current_button + 1) % len(buttons)
                    elif event.key == pygame.K_UP:
                        self.current_button = (self.current_button - 1) % len(buttons)
                    elif event.key == pygame.K_RETURN:
                        if self.current_button == 0:
                            return "Play"
                        elif self.current_button == 1:
                            return "Help"
                        elif self.current_button == 2:
                            pygame.quit()
                            sys.exit()

            for i, button in enumerate(buttons):  # zmena barvy tlacitka
                if i == self.current_button:
                    buttons[i] = (button[0], RED)
                else:
                    buttons[i] = (button[0], WHITE)

            pygame.display.update()

    def draw_text(self, text, font, color, x, y):
        """
        vykreslovani textu
        """
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_obj, text_rect)