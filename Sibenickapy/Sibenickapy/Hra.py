import pygame
import sys
import os
from random import randint
from typing import List
import random
import json
from os.path import dirname, join, realpath




class BaseGame:
    """
    Zakladni trida pro hru
    """
    def __init__(self, words_file, scores_file): # konstruktor, definuje vsechny prvky pouzite ve hre
        """
        inicializuje zakladni hru se vsemi potrebnymi prvky
        """
        self.keyboard_layout = self.generate_keyboard_layout()
        self.key_width = 70 
        self.key_height = 70  
        self.margin = 10 
        self.words = words_file
        self.scores_file = scores_file
        self.word = []
        self.guess = []
        self.guessed_letters = []
        self.lives = 10
        self.current_background = 0
        self.background_images = self.load_background_images()
        self.game_over = False  
        self.score = 0 
        self.streak = 1  
        
        font_size = 50
        current_dir = os.path.dirname(__file__)
        font_path = os.path.join(current_dir, "Hovna", "CURLZ.ttf")         # nacitani fontu
        self.custom_font = pygame.font.Font(font_path, font_size)
        
        self.scores = self.load_scores_from_file(scores_file)
        
    
    def load_words_from_file(self, file_path):
        """
        Nacitani slov ze souboru
        """
        with open(join(dirname(realpath(__file__)), file_path), "r", encoding = "utf_8") as file:
            words = [word.strip() for word in file.readlines()]
        return words

    def load_scores_from_file(self, file_path):
        """
        Nacitani skore ze souboru
        """
        try:
            with open(join(dirname(realpath(__file__)), "score.txt"), "r", encoding = "utf_8") as file:
                scores = [int(i) for i in file.readlines()]
        except FileNotFoundError:
            scores = [0, 0, 0]
        return scores

    def save_scores_to_file(self):
        """
        Ukladani skore do souboru
        """
        with open(self.scores_file, 'score.txt') as file:
            json.dump(self.scores, file)

    def update_scores(self, new_score):
        """
        Aktualizovani noveho skore
        """
        for place, score in self.scores.items():
            if new_score > score:
                self.scores[place] = new_score
                break
        self.save_scores_to_file()

    def generate_keyboard_layout(self):
        """
        Rozlozeni klavesnice
        """
        
        top_row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        middle_row = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        bottom_row = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        
        keyboard_layout = {}

       
        for i, key in enumerate(top_row):           # rozlozeni jednotlivych radku
            keyboard_layout[key] = (i, 0)

        
        for i, key in enumerate(middle_row):
            keyboard_layout[key] = (i + 0.5, 1)

        
        for i, key in enumerate(bottom_row):
            keyboard_layout[key] = (i + 1.5, 2)

        return keyboard_layout

    def load_background_images(self):               
        """
        Nacteni pozadi
        """
        current_dir = os.path.dirname(__file__)
        image_paths = [
            os.path.join(current_dir, "Hovna", "west.png"),
            *[os.path.join(current_dir, "Hovna", f"Ziv{i}.png") for i in range(1, 11)]
        ]
        background_images = [pygame.image.load(path).convert() for path in image_paths]
        return background_images

    def handle_key_event(self, event):  
        """
        Kontrola, jestli je stlacena klavesa na klavesnici 
        a pak ho prida do listu guessed_letters
        """
        if not self.game_over: 
            if event.type == pygame.KEYDOWN:
                if event.unicode in self.keyboard_layout:
                    pressed_letter = event.unicode
                    if pressed_letter not in self.guessed_letters:
                        self.guessed_letters.append(pressed_letter)
                        self.guess_letter(pressed_letter)

    def guess_letter(self, letter):
        """
        Hadani slov a ubirani zivotu (pridavani obrazovek)
        """
        if letter not in self.word:
            self.lives -= 1
            self.streak = 1
            if self.lives < 10:
                self.current_background += 1
                if self.current_background >= len(self.background_images):
                    self.current_background = len(self.background_images) - 1
        else:
            self.score += self.streak
            self.streak += 1
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guess[i] = letter
            self.guessed_letters.append(letter)

        if "#" not in self.guess:  # kontrola, jestli byla vsechna pismena uhadnuta
            self.word = []  # resetuje slovo
            self.guessed_letters = []  
            self.start_game()  # spusti novou hru
            
            self.current_background = min(self.current_background, len(self.background_images) - 1)

        
        pygame.display.update()

    def render_keyboard_layout(self, screen): 
        """
        Vykresleni klavesnice na obrazovce
        """
        max_keys_per_row = 10
        row_count = (len(self.keyboard_layout) + max_keys_per_row - 1) // max_keys_per_row
        total_width = max_keys_per_row * (self.key_width + self.margin)
        total_height = row_count * (self.key_height + self.margin)
        start_x = (800 - total_width) // 2
        start_y = 800 - total_height - 20

        row_index = 0
        col_index = 0
        for letter, (x, y) in self.keyboard_layout.items():
            x_pos = start_x + x * (self.key_width + self.margin)
            y_pos = start_y + y * (self.key_height + self.margin)
            rect = pygame.Rect(x_pos, y_pos, self.key_width, self.key_height)

            if letter in self.guessed_letters:  # zmena barvy pismene
                color = (0, 0, 0)  
            else:
                color = (255, 255, 255) 
            pygame.draw.rect(screen, color, rect)

            
            text = self.custom_font.render(letter, True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

            col_index += 1
            if col_index >= max_keys_per_row:
                col_index = 0
                row_index += 1

        pygame.display.update()

    def start_game(self):
        """
        Zacatek nove hry
        """
        self.word = list(self.words[randint(0, len(self.words) - 1)])  # vybrani nahodneho slova z listu
        self.guess = ["#"] * len(self.word)  # hadane slovo - delka slova v # podle delky slova z listu
        self.guessed_letters = []
        self.current_background = min(self.current_background, len(self.background_images) - 1)

    def show_current_background(self, screen):
        """
        Nacteni spravneho pozadi
        """
        screen.blit(self.background_images[self.current_background], (0, 0))

    def show_game_status(self, screen):
        """
        Vykreslovani na obrazovku
        """
        
        guessed_word = [letter if letter in self.guessed_letters else '#' for letter in self.word]
        guessed_word_text = self.custom_font.render (" ".join(guessed_word), True, (255, 255, 255))
        guessed_word_rect = guessed_word_text.get_rect(center=(400, 400))
    
        score_text = self.custom_font.render (f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(20, 20))
    
        screen.blit(guessed_word_text, guessed_word_rect)
        screen.blit(score_text, score_rect)
        
        pygame.display.update([guessed_word_rect, score_rect])

    def check_game_over(self): 
        """
        Kontrola, zda hraci dosly zivoty
        """
        if self.lives <= 0:
            return "lost"
        elif "#" not in self.guess:
            return "won"
    
        if self.current_background == len(self.background_images) - 1:  # Check if the last background is reached
            return "lost"
    
        return None

    def update_background(self):
        """
        Nacteni pozadi pokud hrac prohral
        """
        if self.check_game_over() == "lost": 
            self.game_over = True

    def show_ending_window(self, screen): 
        """
        Obrazovka, po prohre hrace
        """
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "Hovna", "over.jpg")
        ending_image = pygame.image.load(image_path).convert()
        screen.blit(ending_image, (0, 0))
    
        
        font = pygame.font.Font(None, 50)
        game_over_text = self.custom_font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(400, 200))
        screen.blit(game_over_text, game_over_rect)

        
        score_text = self.custom_font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(400, 300))
        screen.blit(score_text, score_rect)
        
        
        top_scores_text = self.custom_font.render("Top Scores:", True, (255, 255, 255))
        top_scores_rect = top_scores_text.get_rect(center=(400, 400))
        screen.blit(top_scores_text, top_scores_rect)
        
        y_offset = 450
        for score in enumerate(self.scores):
            score_text = self.custom_font.render(str(score[0] + 1) + ". - " + str(score[1]), True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(400, y_offset))
            screen.blit(score_text, score_rect)
            y_offset += 50

        
        pygame.display.update()

        while True:                             # zavreni hry
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()



class EasyGame(BaseGame):
    """
    Trida pro jednoduche nastaveni hry, steje jako zakladni
    """
    def __init__(self, words_file, scores_file):
        super().__init__(words_file, scores_file)
        self.words = self.load_words_from_file("words1.txt")
        

    def start_game(self):
        super().start_game()
        

class MediumGame(BaseGame):
    """
    Trida pro stredne tezke nastaveni hry
    """
    def __init__(self, words_file, scores_file):
        super().__init__(words_file, scores_file)
        self.words = self.load_words_from_file("words1.txt")
        self.current_background = 4
        
        

    def start_game(self):
        super().start_game()
        

class HardGame(BaseGame):
    """
    Trida pro tezke nastaveni hry
    """
    def __init__(self, words_file, scores_file):
        super().__init__(words_file, scores_file)
        self.words = self.load_words_from_file("words2.txt")
        self.current_background = 4
   

        

    def start_game(self):
        super().start_game()
        

