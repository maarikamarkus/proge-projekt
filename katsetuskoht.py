from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def cinamon_aeg_film(cinamon_src):
    cinamon_kinokava = BeautifulSoup(cinamon_src, 'lxml')

    cinamon_kavarida = cinamon_kinokava.find_all('div', class_="schedule__row")

    #print("Cinamoni tänane kinokava: ")
    cinamon_aeg_film = {}
    for cinamon_rida in cinamon_kavarida:
        cinamon_kellaaeg = cinamon_rida.find('div', class_="schedule__time")
        cinamon_film = cinamon_rida.find('div', class_="schedule__film__name")
        cinamon_aeg_film[cinamon_kellaaeg.text.strip()] = cinamon_film.text.strip()
    for cinamon_el in cinamon_aeg_film:
        #return cinamon_aeg_film.items() 
        return(cinamon_el + " \n " + cinamon_aeg_film[cinamon_el])

   # print("\n")
        
cinamon_src = requests.get("https://cinamonkino.com/tasku/ajakava/ee").text

def cinamon():
    cinamonkava = cinamon_aeg_film(cinamon_src)
    tekst.config(text=cinamonkava)
    
#print("\n")


# GUI w/tkinter

aken = Tk()

silt = Label(text="Tartu tänane kinokava")
silt.pack(side=TOP, fill=X)

menüü = Frame(aken)

#cinamon = Label(menüü, text="Cinamon")
#cinamon.config(text=cinamon_aeg_film(cinamon_src))
cinamon = Button(menüü, text="Cinamoni kinokava", command=cinamon)
cinamon.pack(side=LEFT)

tekst = ttk.Label(text="Tere, ma olen tekst.")
tekst.pack()

menüü.pack(side=TOP, fill=X)

aken.mainloop()


