from station import Station, ListStations
import functions as fct
import pygame


class Ligne:
    def __init__(self, type_="", name="", color="", l_s={}):
        self.type = type_   # M=Metro, R=Rer, T=Tram, B=Bus
        self.name = name
        self.color = color
        self.id = self.type + self.name

        self.ligne_stations = l_s  # {station1:{s_voisin1,s_voisin2}, station2:, ...}

    def add_station(self, station):
        if station not in self.ligne_stations:
            self.ligne_stations[station] = set()

    def add_neighbor_to_station(self, station, neighbor):
        self.ligne_stations[station].add(neighbor)
        self.ligne_stations[neighbor].add(station)


class ListLignes:
    def __init__(self):
        self.all_lignes = set()  # {Ligne(), Ligne(), ...} ?

    def save_list_lignes(self):
        with open("storage_lignes.txt", 'w') as f:
            for ligne in self.all_lignes:
                f.write(ligne.type + ';' + ligne.name + ';' + ligne.color)
                for l_station in ligne.ligne_stations.keys():
                    f.write(';' + l_station.name)
                    for voisin in ligne.ligne_stations[l_station]:
                        f.write(',' + voisin.name)
                f.write('\n')

    def load_list_lignes(self, all_stations):
        with open("storage_lignes.txt", 'r') as f:
            line = f.readline()
            while line != "":
                L = line.split(';')
                thing = {}
                for i in range(3, len(L)):
                    txt = L[i]
                    T = txt.split(',')
                    thing[all_stations.find_station_by_name(T[0])] = set()
                    for voisin in T[1:]:
                        thing[all_stations.find_station_by_name(T[0])].add(all_stations.find_station_by_name(voisin))

                self.all_lignes.add(Ligne(L[0], L[1], L[2], thing))
                line = f.readline()

    def find_ligne_by_id(self, id_):
        for ligne in self.all_lignes:
            if ligne.id == id_:
                return ligne

    def add_ligne(self, type_, name, color, l_s={}):
        self.all_lignes.add(Ligne(type_, name, color, l_s))

    def remove_ligne_by_id(self, id_):
        if self.find_ligne_by_id(id_):
            self.all_lignes.remove(self.find_ligne_by_id(id_))

    def add_station_to_ligne(self, id_ligne, station):
        if self.find_ligne_by_id(id_ligne):
            (self.find_ligne_by_id(id_ligne)).add_station(station)

    def display_all_lignes(self, screen):           # !!!!!!!!! To test if it's work
        for ligne in self.all_lignes:
            for l_station in ligne.ligne_stations.keys():
                l_station.display_a_station(screen, ligne.color)

                for voisin in ligne.ligne_stations[l_station]:
                    pygame.draw.line(screen, ligne.color, l_station.position, voisin.position, 1)
