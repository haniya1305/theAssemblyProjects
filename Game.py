import time
import random
import sys
import pygame
from pygame.locals import *

class Game:

    def __init__(self):
        self.breadth = 800
        self.length = 600
        self.input = ''
        self.string1 = ''
        self.reset = True
        self.active = False
        self.start = 0
        self.total_time = 0
        self.accuracy = ''
        self.output = ''
        self.end = False

        pygame.init()
        self.open_img = pygame.image.load('background.jpg')
        self.open_img = pygame.transform.scale(self.open_img, (self.breadth, self.length))

        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.length, self.breadth))

        self.screen = pygame.display.set_mode((self.breadth, self.length))
        pygame.display.set_caption('Typing Speed Test')

    def display(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.breadth / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_text(self):
        phrases = ["This is a test to check your typing skills and you are doing great!", "Welcome to the typing test! Good luck and have fun.", "Once upon a time, there was a king who had seven beautiful children.", "Hello and Welcome to The Assembly. We hope you have fun!"]
        string1 = random.choice(phrases)
        return (string1)

    def results(self, screen):
        if (self.end == False):
            # Calculate time
            self.total_time = time.time() - self.start
            # Calculate accuracy
            count = 0
            for i, c in enumerate(self.string1):
                try:
                    if self.input[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.string1) * 100

            self.output = 'Time: ' + str(round(self.total_time)) + " secs   Accuracy: " + str(round(self.accuracy)) + "%"

            # Reset Button
            self.display(screen, "Reset", self.length - 150, 30, (255, 0, 0))

            pygame.display.update()

    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))

        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.end = False

        self.input = ''
        self.string1 = ''
        self.start = 0
        self.total_time = 0

        # Get random sentence
        self.string1 = self.get_text()
        if (not self.string1):
            self.reset_game()
        # drawing heading
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        msg = "Typing Speed Test"
        self.display(self.screen, msg, 80, 80, (255, 213, 102))
        # draw the rectangle for input box
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        # draw the sentence string
        self.display(self.screen, self.string1, 200, 28, (240, 240, 240))

        pygame.display.update()

    def run(self):
        self.reset_game()

        self.running = True
        while (self.running == True):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, (255, 0, 100), (70, 250, 650, 50), 3)
            # update the text of user input
            self.display(self.screen, self.input, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # position of input box
                    if (x >=70 and x <=650 and y>=250 and y<=300):
                        self.active = True
                        self.input = ''
                        self.start = time.time()
                        # position of reset box
                    if (x >=400 and x <=500 and y>=450 and self.end):
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()


                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input)
                            self.results(self.screen)
                            print(self.output)
                            self.display(self.screen, self.output, 350, 28, (255, 70, 70))
                            self.end = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input = self.input [:-1]
                        else:
                            try:
                                self.input += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(50)