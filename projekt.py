# programmeerimise aine projekt
# idee luua programm, mis leiab kõige odavama kinokülastuse variandi tartus
# selleks kasutame lisandmoodulit beautifulsoup, mis tuleb eraldi endale lisada
# samuti tuleb lisanda requests -- tools > manage packages.. > otsingusse requests > install
# ja samamoodi lisada ka lxml
# esialgne abistav info: https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python

# https://www.youtube.com/watch?v=ng2o98k983k -- hea video beautifulsoupi kohta
# https://www.youtube.com/watch?v=87Gx3U0BDlo -- veel head infot

# soup.prettify() teeb html koodile õiged taanded
# status_code, kui == 200, siis saame ligi sellele lehele
#print(source.status_code)
# find_all, '...' leiab kõik ... sellelt lehelt

# cinamon
# class = "schedule__film__name" - kinokavas oleva filmi class, NB! 2 alakriipsu
# class = "pageSeatPlan_ticketTypes--standard" -- tavaline pilet
# class = "pageSeatPlan_ticketTypes--love" -- loveseat pilet

# apollo kino - Kati
# ekraan - Maarika

# kõigepealt proovime cinamoni lehelt vajaliku info kätte saada

from bs4 import BeautifulSoup
import requests

# cinamon
# request.get() abil saame veebilehe kätte
cinamon_src = requests.get("https://cinamonkino.com/tasku/ajakava/ee").text

# BeautifulSoup annab meile selle lehe html koodi
cinamon_kinokava = BeautifulSoup(cinamon_src, 'lxml')

cinamon_kavarida = cinamon_kinokava.find_all('div', class_="schedule__row")
#cinamon_kellaajad = cinamon_kinokava.find_all('div', class_="schedule__time")
#cinamon_filmid = cinamon_kinokava.find_all('div', class_="schedule__film__name")

# sõnastik tänase kinokavaga, kellaaeg:film, näitab ainult täna veel tulevaid filme
# ei tea, mis teeb siis, kui täna enam midagi kavas pole, ilmselt peab mingi erindi varianti kasutama
print("Cinamoni tänane kinokava: ")
cinamon_aeg_film = {}
for cinamon_rida in cinamon_kavarida:
    #print(cinamon_rida)
    cinamon_kellaaeg = cinamon_rida.find('div', class_="schedule__time")
    cinamon_film = cinamon_rida.find('div', class_="schedule__film__name")
    cinamon_aeg_film[cinamon_kellaaeg.text.strip()] = cinamon_film.text.strip()
for cinamon_el in cinamon_aeg_film:
    print(cinamon_el + " : " + cinamon_aeg_film[cinamon_el])
#print(cinamon_aeg_film)
print("\n")

#filmid_hulk = set()
#for film in filmid:
#    filmid_hulk.add(film.text.strip())

#print(filmid_hulk)
#print(len(filmid_hulk))
#print(filmide_arv)
    
# ekraan
# ei ole kindel, et ta alati ekraani näitab, tundub, et vaatab arvuti asukoha järgi
# aadressis ei ole tartut ega ekraani märgitud, olgugi et näitab ekraani valikut
ekraan_src = requests.get("https://www.forumcinemas.ee/movies/showtimes").text

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
    
    
    
    
    
# otsime lingi, mille sisu on Kinokava ja siis võtame selle href-i väärtuse ka
#for link in links:
#    if "Kinokava" in link.text:
#        print(link)
#        print(link.attrs['href'])