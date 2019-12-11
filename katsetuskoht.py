from bs4 import BeautifulSoup
import requests
from tkinter import *

def cinamon_aeg_film(cinamon_src):
    # BeautifulSoup annab meile selle lehe html koodi
    cinamon_kinokava = BeautifulSoup(cinamon_src, 'lxml')

    cinamon_kavarida = cinamon_kinokava.find_all('div', class_="schedule__row")
    #cinamon_kellaajad = cinamon_kinokava.find_all('div', class_="schedule__time")
    #cinamon_filmid = cinamon_kinokava.find_all('div', class_="schedule__film__name")

    print("Cinamoni tänane kinokava: ")
    cinamon_aeg_film = {}
    for cinamon_rida in cinamon_kavarida:
        #print(cinamon_rida)
        cinamon_kellaaeg = cinamon_rida.find('div', class_="schedule__time")
        cinamon_film = cinamon_rida.find('div', class_="schedule__film__name")
        cinamon_aeg_film[cinamon_kellaaeg.text.strip()] = cinamon_film.text.strip()
    for cinamon_el in cinamon_aeg_film:
        print(cinamon_el + " : " + cinamon_aeg_film[cinamon_el])
    print("\n")
        
cinamon_src = requests.get("https://cinamonkino.com/tasku/ajakava/ee").text

def cinamon():
    cinamon_aeg_film(cinamon_src)
#print("\n")

def ekraan_aeg_film(ekraan_src):

    ekraan_kinokava = BeautifulSoup(ekraan_src, 'lxml')
    ekraan_kavarida = ekraan_kinokava.find_all('div', class_="row show-list-item-inner")

    print("Kino Ekraani tänane kinokava on: ")
    ekraan_aeg_film = {}
    for ekraan_rida in ekraan_kavarida:
        ekraan_kellaaeg = ekraan_rida.find('h2', class_="showTime").text.strip()
        ekraan_film = ekraan_rida.find('span', class_="name-part").text.strip()
        ekraan_aeg_film[ekraan_kellaaeg] = ekraan_film

    for ekraan_el in ekraan_aeg_film:
        print(ekraan_el + " : " + ekraan_aeg_film[ekraan_el])
    print("\n")
        
ekraan_src = requests.get("https://www.forumcinemas.ee/movies/showtimes").text

def ekraan():
    ekraan = ekraan_aeg_film(ekraan_src)
#print("\n")


# GUI w/tkinter

aken = Tk()

silt = Label(text="Tartu tänane kinokava")
silt.pack(side=TOP, fill=X)

menüü = Frame(aken)

cinamon = Button(menüü, text="Cinamoni kinokava", command=cinamon)
cinamon.pack(side=LEFT)
ekraan = Button(menüü, text="Ekraani kinokava", command=ekraan)
ekraan.pack(side=LEFT)

menüü.pack(side=TOP, fill=X)

aken.mainloop()


