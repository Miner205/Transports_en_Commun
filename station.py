import pygame
import functions as fct


class Station:
    def __init__(self, name="", x=None, y=None):
        self.name = name
        self.position = (x, y)

    def set_position(self, x, y):
        self.position = (x, y)

    def display_a_station(self, screen, color, zoom, distance_off_screen, x_slide, y_slide, show_stations_names):
        fct.pygame_draw_star(screen, color, (zoom*self.position[0]-int(distance_off_screen[0]*zoom)+x_slide,
                                             zoom*self.position[1]-int(distance_off_screen[1]*zoom)+y_slide),
                             5*zoom, int(1*zoom))
        if show_stations_names:  # + display name station ; with a toggle button
            text_font = pygame.font.Font(None, int(24*(zoom/2)))
            text_surface = text_font.render(self.name, True, (0, 0, 0))
            screen.blit(text_surface, (((5+len(self.name)*11)/2)*zoom/2+zoom*(self.position[0]-(len(self.name)*11)/2)-int(distance_off_screen[0]*zoom)+x_slide,
                                       zoom*(self.position[1])-int(distance_off_screen[1]*zoom)+y_slide-20*(zoom/2)))


class ListStations:
    def __init__(self):
        self.all_stations = set()  # {Station("aa",0,8), Station("kk",99,-5)}

    def save_list_stations(self):
        with open("storage_stations.txt", 'w') as f:
            for station in self.all_stations:
                f.write(station.name + ';' + str(station.position[0]) + ';' + str(station.position[1]))
                f.write('\n')

    def load_list_stations(self):
        with open("storage_stations.txt", 'r') as f:
            line = f.readline()
            while line != "":
                L = line.strip('\n').split(';')
                self.all_stations.add(Station(L[0], int(L[1]), int(L[2])))
                line = f.readline()

    def find_station_by_name(self, name):
        for station in self.all_stations:
            if station.name == name:
                return station

    def add_station(self, name, x, y):
        self.all_stations.add(Station(name, x, y))

    def remove_station_by_name(self, name):
        if self.find_station_by_name(name):
            self.all_stations.remove(self.find_station_by_name(name))
