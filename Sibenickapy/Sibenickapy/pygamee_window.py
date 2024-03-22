import pygame
import os
from Mennu import Menu
from gamee_window import GameWindow
from hangman_window import HangmanWindow


class PygameWindow:
    """
    Tato trida predstavuje samotne hlavni okno teto hry, inicializuje se zde Pygame prostredi,
    hlavni ovladani hry
    """
    
    def __init__(self):
        """
        inicializace Pygame okna a potrebnych assetu
        """
        pygame.init()
        self.window_size = (800, 800)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("My Pygame Window")
        self.load_background_image()

        font_size = 50
        current_dir = os.path.dirname(__file__)
        font_path = os.path.join(current_dir, "Hovna", "CURLZ.ttf")  
        self.custom_font = pygame.font.Font(font_path, font_size)

        music_path = os.path.join(current_dir, "Hovna", "vsude.mp3")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)

    def load_background_image(self):
        """
        nacita pozadi
        """

        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "Hovna", "west.png")
        self.background_image = pygame.image.load(image_path).convert()

    def run(self):
        """
        
        """
        while True:
            menu = Menu(self.screen, self.background_image, self.custom_font)
            choice = menu.run()
            if choice == "Play":
                game_window = GameWindow(self.screen, self.background_image)
                game_window.run(self.screen, self.background_image)
            elif choice == "Help":
                self.show_help_screen()

    def show_help_screen(self):
        """
        zobrazuje obrazovku s instrukcemi ke hre
        """
        self.screen.blit(self.background_image, (0, 0))

        help_text = [
            "Save your life!",
            "Guess the letters in the words!",
            "Use letter keys to select letters",
        ]

        screen_width, screen_height = self.screen.get_size()
        text_height = len(help_text) * 40
        start_y = (screen_height - text_height) // 2

        for line in help_text:
            text_surface = self.custom_font.render(line, True, (255, 255, 255))

            text_width = text_surface.get_width()
            start_x = (screen_width - text_width) // 2
            self.screen.blit(text_surface, (start_x, start_y))
            start_y += 40

        pygame.display.update()

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return  
                    


if __name__ == "__main__":
    from pygamee_window import PygameWindow
    pygame_window = PygameWindow()
    pygame_window.run()
