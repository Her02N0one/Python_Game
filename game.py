import pygame

def initWindow():
    c = open("window.txt", "r")
    if c.mode == "r":
        config = c.readlines()
        (width, height) = (config[1])


    screen = pygame.display.set_mode((width, height))
    pygame.display.
    pygame.display.flip()
    input()

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
def render():


initWindow()
def run():
    Running = True
    while Running:
        update()
        render()
