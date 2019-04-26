import pygame

def initWindow():
    c = open(window.txt, "r")
    if f.mode == "r":
        contents = f.read()
        print(contents)
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    input()

def run():
    initWindow()
