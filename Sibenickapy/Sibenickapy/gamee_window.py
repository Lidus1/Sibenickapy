import pygame
import os
from Hra import EasyGame, MediumGame, HardGame
from hangman_window import HangmanWindow



class GameWindow:
    """
    Trida reprezentujici okno pro vybirani obtiznosti
    """
    def __init__(self, screen, background_image):
        """
        Inicializuje okno s danym pozadim
        """
        self.screen = screen
        self.background_image = background_image

    def run(self,screen,background_image):
        """
        Spousti hlavni cyklus
        """
        running = True

        current_dir = os.path.dirname(__file__)

        image1_path = os.path.join(current_dir, "Hovna", "easy.png")  # cesta k obrazkum
        image2_path = os.path.join(current_dir, "Hovna", "medium.png")
        image3_path = os.path.join(current_dir, "Hovna", "hard.png")

        image1 = pygame.image.load(image1_path).convert_alpha()  # nacteni obrazu
        image2 = pygame.image.load(image2_path).convert_alpha()
        image3 = pygame.image.load(image3_path).convert_alpha()

        image_width = 200  # pozice obrazku
        spacing = 20
        total_width = image_width * 3 + spacing * 2
        start_x = (self.screen.get_width() - total_width) // 2
        image_y = 50
        current_image = 0

        while running:  # pohyb mezi obrazky, spusteni jednotlivych obtiznosti podle class
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        difficulty_classes = [EasyGame, MediumGame, HardGame]
                        selected_difficulty_class = difficulty_classes[current_image]
                        hangman_window = HangmanWindow(screen, background_image, words_file="words.txt", scores_file="scores.json")
                        hangman_window.run(selected_difficulty_class)
                    elif event.key == pygame.K_LEFT:
                        current_image = (current_image - 1) % 3
                    elif event.key == pygame.K_RIGHT:
                        current_image = (current_image + 1) % 3

            self.screen.blit(self.background_image, (0, 0))

            image1_rect = self.screen.blit(image1, (start_x, image_y))
            image2_rect = self.screen.blit(image2, (start_x + image_width + spacing, image_y))
            image3_rect = self.screen.blit(image3, (start_x + 2 * (image_width + spacing), image_y))

            if current_image == 0:  # ohraniceni kolem obrazku
                pygame.draw.rect(self.screen, (255, 0, 0), image1_rect, 2)
            elif current_image == 1:
                pygame.draw.rect(self.screen, (255, 0, 0), image2_rect, 2)
            elif current_image == 2:
                pygame.draw.rect(self.screen, (255, 0, 0), image3_rect, 2)

            pygame.display.update()