import pygame
class Game:

    def __init__(self):
        initWindow()

    def __del__(self):
        del window

    def initWindow():
        c = open("window.txt", "r")
        if c.mode == "r":
            config = c.readlines()
            (width, height) = (config[1])
            title = (config[0])

        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        pygame.display.flip()

    def update():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    def render():
          screen.fill(BLACK)
          pygame.display.flip()

    def run():
        Running = True
        while Running:
            update()
            render()
    pygame.quit()
