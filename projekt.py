# programmeerimise aine projekt
# idee luua programm, mis leiab kõige odavama kinokülastuse variandi tartus
# selleks kasutame lisandmoodulit beautifulsoup, mis tuleb eraldi endale lisada
# samuti tuleb lisanda requests -- tools > manage packages.. > otsingusse requests > install
# ja samamoodi lisada ka lxml

# apollo kino - Kati
# ekraan - Maarika
# cinamon - Maarika

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
        
# request.get() abil saame veebilehe kätte
cinamon_src = requests.get("https://cinamonkino.com/tasku/ajakava/ee").text

def cinamon():
    cinamon_aeg_film(cinamon_src)
#print("\n")
#cinamon_kava = cinamon()

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




#APOLLO
def apollo_aeg_film(apollo_src):
    apollo_kinokava = BeautifulSoup(apollo_src, 'lxml')
    apollo_kavarida = apollo_kinokava.find_all('div', class_="panel-body")

    print("Kino Apollo Eedeni tänane kinokava on: ")
    for apollo_rida in apollo_kavarida:
        apollo_film = apollo_rida.find('h2', class_="list-item-desc-title")
        apollo_kellaaeg = apollo_rida.find("div", class_="btn-group")
        try:
            apollo_filminimi = apollo_film.find("a", href = True).text.strip()
            apollo_filminimi =re.sub(" +", " ", apollo_filminimi)
            apollo_kell = (apollo_kellaaeg.find("span")).text.strip()
            if apollo_kell == "Tähestikuline":
                a = 0
            else:
                print(apollo_kell, ":" , apollo_filminimi)
        except:
            break
    print("\n")
apollo_src = requests.get("https://www.apollokino.ee/?TheatreArea=1014&SetHome=1").text

def apollo():
    apollo = apollo_aeg_film(apollo_src)
    
# LÕUNAKESKUS
def lounakeskus_aeg_film(lounakeskus_src):
    lounakeskus_kinokava = BeautifulSoup(lounakeskus_src, 'lxml')
    lounakeskus_kavarida = lounakeskus_kinokava.find_all('div', class_="panel-body")

    print("Kino Apollo Lõunakeskuse tänane kinokava on: ")
    for lounakeskus_rida in lounakeskus_kavarida:
        lounakeskus_film = lounakeskus_rida.find('h2', class_="list-item-desc-title")
        lounakeskus_kellaaeg = lounakeskus_rida.find("div", class_="btn-group")
        try:
            lounakeskus_filminimi = lounakeskus_film.find("a", href = True).text.strip()
            lounakeskus_filminimi =re.sub(" +", " ", lounakeskus_filminimi)
            lounakeskus_kell = (lounakeskus_kellaaeg.find("span")).text.strip()
            if lounakeskus_kell == "Tähestikuline":
                a = 0
            else:
                print(lounakeskus_kell, ":" , lounakeskus_filminimi)
        except:
            break
    print("\n")

lounakeskus_src = requests.get("https://www.apollokino.ee/?TheatreArea=1011&SetHome=1").text

def lounakeskus():
    lounakeskus = lounakeskus_aeg_film(lounakeskus_src)

# Filmi otsing

#film = input("Millise filmi kellaaegu sooviksid näha? ")
#
#for a in cinamon_aeg_film:
#    film1 = cinamon_aeg_film.get(a)
#    if film == film1:
#        print(a,":",film, "(Cinamon)")
#
#for a in ekraan_aeg_film:
#    film1 = ekraan_aeg_film.get(a)
#    if film == film1:
#        print(a,":",film, "(Ekraan)")
#



# GUI w/tkinter

aken = Tk()

silt = Label(text="Tartu tänane kinokava")
silt.pack(side=TOP, fill=X)

menüü = Frame(aken)

cinamon = Button(menüü, text="Cinamoni kinokava", command=cinamon)
cinamonkava = Label(menüü, text=cinamon)
cinamon.pack(side=LEFT)

ekraan = Button(menüü, text="Ekraani kinokava", command=ekraan)
ekraan.pack(side=LEFT)

apollo = Button(menüü, text="Apollo kinokava", command=apollo)
apollo.pack(side=LEFT)

lounakeskus = Button(menüü, text="Lõunakeskuse kinokava", command=lounakeskus)
lounakeskus.pack(side=LEFT)

menüü.pack(side=TOP, fill=X)

aken.mainloop()








    
# otsime lingi, mille sisu on Kinokava ja siis võtame selle href-i väärtuse ka
#for link in links:
#    if "Kinokava" in link.text:
#        print(link)
#        print(link.attrs['href'])

#filmid_hulk = set()
#for film in filmid:
#    filmid_hulk.add(film.text.strip())

#print(filmid_hulk)
#print(len(filmid_hulk))
#print(filmide_arv)