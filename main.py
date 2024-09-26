import pygame
from station import ListStations, Station
from ligne import ListLignes, Ligne
from button import Button
from textezone import TextZone
import functions as fct
# from parameters import Options

# To run to start the thing..



# Project : Concevoir une solution pour permettre aux usagers du métro d'identiier
# les lignes de métro les plus sonores ( cartographie acoustique des lignes de métro)


#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


if __name__ == '__main__':
    print('PyCharm')


# # TO DO :
#
# github
#


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60

# Create a window
pygame.display.set_caption("Metros plan")
width, height = 1820, 980   # 1080, 720
screen = pygame.display.set_mode((width, height))   # , pygame.RESIZABLE

# background
# background = pygame.image.load("assets/background.jpeg")


running = True

all_stations = ListStations()
all_lignes = ListLignes()
all_stations.load_list_stations()
all_lignes.load_list_lignes(all_stations)

b = TextZone(50, 500, 'rr')

while running:

    # display the background // faire un quadrillage
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, height))
    for w in range(0, width+1, 51):
        pygame.draw.line(screen, (0, 0, 0), (w, 0), (w, height), 1)
        for h in range(0, height + 1, 51):
            fct.pygame_draw_cross(screen, (255, 0, 0), (w, h))
    for h in range(0, height+1, 51):
        pygame.draw.line(screen, (0, 0, 0), (0, h), (width, h), 1)
    # screen.blit(background, (0, 0))

    # get the current time
    current_time = pygame.time.get_ticks() // 1000
    # print the current time :
    font = pygame.font.SysFont("ArialBlack", 20)
    text = font.render('Time : {} s'.format(current_time), True, (0, 0, 0))
    screen.blit(text, (30, 20))

    # if running: maze.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            all_stations.save_list_stations()
            all_lignes.save_list_lignes()
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            all_stations.save_list_stations()
            all_lignes.save_list_lignes()
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            b.use(event)

        """if event.type == pygame.KEYDOWN:
            maze.keys_pressed[event.key] = True

        if event.type == pygame.KEYUP:
            maze.keys_pressed[event.key] = False"""

        # maze.update(event)

    if running:
        b.draw(screen)
        all_lignes.display_all_lignes(screen)

    # Update the screen
    if running:
        pygame.display.flip()
        clock.tick(FPS)
