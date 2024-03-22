import pygame
import os
from Hra import EasyGame, MediumGame, HardGame
from Hra import BaseGame


class HangmanWindow:
    """
    Tato trida reprezentuje okno samotne hry.
    """
    def __init__(self, screen, background_image, words_file, scores_file):
        """
        Inicializuje okno hry s danym pozadim, soubory se slovy a skorem
        """
        self.screen = screen
        self.background_image = background_image
        self.words_file = words_file
        self.scores_file = scores_file

    def run(self, game_class):
        """
        Spousi hlavni cyklus hry
        """
        
        running = True
        game_instance = game_class(self.words_file, self.scores_file)

        game_instance.start_game()  

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                game_instance.handle_key_event(event)

            self.screen.fill((0, 0, 0))  
            game_instance.show_current_background(self.screen)
            game_instance.render_keyboard_layout(self.screen)
            game_instance.show_game_status(self.screen)

            pygame.display.update()

            game_result = game_instance.check_game_over()  
            if game_result is not None:
                if game_result == "lost":
                    print("You lost!")
                    game_instance.show_ending_window(self.screen)
                    pygame.display.flip()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                break
                            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                return  
                    break
                elif game_result == "won":
                    print("You won!")
                    game_instance.start_game()