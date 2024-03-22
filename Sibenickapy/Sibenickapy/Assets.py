import pygame

class Zapni:
    def __init__(self):
        
        self.font = pygame.font.Font("Hovna/CURLZ.ttf", 32)
        self.klaves = pygame.font.Font("Hovna/Arialn.ttf", 32)
        self.lehka = pygame.image.load("Hovna/easy.png").convert()
        self.stredni = pygame.image.load("Hovna/medium.png").convert()
        self.tezka = pygame.image.load("Hovna/hard.png").convert()
        self.west = pygame.image.load("Hovna/west.png").convert()
        self.Ziv1 = pygame.image.load("Hovna/Ziv1.png").convert()
        self.Ziv2 = pygame.image.load("Hovna/Ziv2.png").convert()
        self.Ziv3 = pygame.image.load("Hovna/Ziv3.png").convert()
        self.Ziv4 = pygame.image.load("Hovna/Ziv4.png").convert()
        self.Ziv5 = pygame.image.load("Hovna/Ziv5.png").convert()
        self.Ziv6 = pygame.image.load("Hovna/Ziv6.png").convert()
        self.Ziv7 = pygame.image.load("Hovna/Ziv7.png").convert()
        self.Ziv8 = pygame.image.load("Hovna/Ziv8.png").convert()
        self.Ziv9 = pygame.image.load("Hovna/Ziv9.png").convert()
        self.Ziv10 = pygame.image.load("Hovna/Ziv10.png").convert()
        pygame.mixer.init()
        self.vsude = pygame.mixer.Sound("Hovna/vsude.mp3")
        self.over = pygame.image.load("Hovna/over.jpg").convert()



    def getFont(self):
        return self.font

    def getLehka(self):
        return self.lehka

    def getStredni(self):
        return self.stredni

    def getTezka(self):
        return self.tezka

    def getKlaves(self):
        return self.klaves

    def getwest(self):
        return self.west

    def getZiv1(self):
        return self.Ziv1

    def getZiv2(self):
        return self.Ziv2

    def getZiv3(self):
        return self.Ziv3

    def getZiv4(self):
        return self.Ziv4

    def getZiv5(self):
        return self.Ziv5

    def getZiv6(self):
        return self.Ziv6

    def getZiv7(self):
        return self.Ziv7

    def getZiv8(self):
        return self.Ziv8

    def getZiv9(self):
        return self.Ziv9

    def getZiv10(self):
        return self.Ziv10

    def getvsude(self):
        return self.vsude

    def getover(self):
        return self.over

