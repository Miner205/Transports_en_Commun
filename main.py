import pygame
from station import ListStations, Station
from ligne import ListLignes, Ligne
from button import Button
from textezone import TextZone
import functions as fct
from tools_menu import ToolsMenu


# To run to start the program


# Memo :
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


if __name__ == '__main__':
    print('main.py launched')


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60

# Create a window
pygame.display.set_caption("Metros plan")
width, height = 1820, 980   # 1080, 720
center = (width//2, height//2)
screen = pygame.display.set_mode((width, height))   # , pygame.RESIZABLE

# background
# background = pygame.image.load("assets/background.jpeg")


running = True
zoom = 1.0
zoom_button = Button(width-20-41*2-3, 20, 41, 41)
dezoom_button = Button(width-20-41, 20, 41, 41)


all_stations = ListStations()
all_lignes = ListLignes()
all_stations.load_list_stations()
all_lignes.load_list_lignes(all_stations)

tools_menu = ToolsMenu()

while running:

    # display the background
    # // faire un quadrillage
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, height))
    for w in range(center[0], -1, int(-51*zoom)):
        pygame.draw.line(screen, (0, 0, 0), (w, 0), (w, height), int(1*zoom))
        for h in range(center[1], -1, int(-51*zoom)):
            fct.pygame_draw_cross(screen, (255, 0, 0), (w, h), 5*zoom, int(1*zoom))
            pygame.draw.line(screen, (0, 0, 0), (0, h), (width, h), int(1*zoom))
        for h in range(center[1], 2 * center[1] + 1, int(51*zoom)):
            fct.pygame_draw_cross(screen, (255, 0, 0), (w, h), 5*zoom, int(1*zoom))
            pygame.draw.line(screen, (0, 0, 0), (0, h), (width, h), int(1*zoom))
    for w in range(center[0], center[0]*2+1, int(51*zoom)):
        pygame.draw.line(screen, (0, 0, 0), (w, 0), (w, height), int(1*zoom))
        for h in range(center[1], -1, int(-51*zoom)):
            fct.pygame_draw_cross(screen, (255, 0, 0), (w, h), 5*zoom, int(1*zoom))
            pygame.draw.line(screen, (0, 0, 0), (0, h), (width, h), int(1*zoom))
        for h in range(center[1], 2 * center[1] + 1, int(51*zoom)):
            fct.pygame_draw_cross(screen, (255, 0, 0), (w, h), 5*zoom, int(1*zoom))
            pygame.draw.line(screen, (0, 0, 0), (0, h), (width, h), int(1*zoom))
    pygame.draw.circle(screen, "green", center, 5*zoom)  # to visualize the center
    # screen.blit(background, (0, 0))

    # get the current time
    current_time = pygame.time.get_ticks() // 1000

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

        if event.type == pygame.MOUSEBUTTONDOWN:  # or event.type == pygame.KEYDOWN:
            tools_menu.update(event)

            if zoom_button.use(event) and zoom < 5.0:
                zoom += 0.5
            if dezoom_button.use(event) and zoom > 1.0:
                zoom -= 0.5

    if running:
        # print the current time :
        font = pygame.font.SysFont("ArialBlack", 20)
        text = font.render('Time : {} s'.format(current_time), True, (0, 0, 0))
        screen.blit(text, (20, 20))

        all_lignes.display_all_lignes(screen, zoom)
        tools_menu.print(screen)

        pygame.draw.rect(screen, (210, 210, 210), (width - 20 - 82 - 6, 20 - 3, 82 + 9, 41 + 6), border_radius=3)
        zoom_button.print(screen)
        fct.pygame_draw_plus(screen, (130, 0, 0), zoom_button.rect.center, zoom_button.rect.w-10, 5)
        dezoom_button.print(screen)
        fct.pygame_draw_minus(screen, (130, 0, 0), dezoom_button.rect.center, dezoom_button.rect.w-10, 5)
        # print the zoom :
        font = pygame.font.SysFont("ArialBlack", 15)
        text = font.render('x{}'.format(zoom), True, (0, 0, 0))
        screen.blit(text, (width-85, -3))

    # Update the screen
    if running:
        pygame.display.flip()
        clock.tick(FPS)
