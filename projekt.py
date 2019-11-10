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

# request.get() abil saame veebilehe kätte
cinamon_src = requests.get("https://cinamonkino.com/tasku/ajakava/ee").text

# BeautifulSoup annab meile selle lehe html koodi
cinamon_kinokava = BeautifulSoup(cinamon_src, 'lxml')

kavarida = cinamon_kinokava.find_all('div', class_="schedule__row")
#kellaajad = cinamon_kinokava.find_all('div', class_="schedule__time")
#filmid = cinamon_kinokava.find_all('div', class_="schedule__film__name")

# sõnastik tänase kinokavaga, kellaaeg:film, näitab ainult täna veel tulevaid filme
# ei tea, mis teeb siis, kui täna enam midagi kavas pole, ilmselt peab mingi erindi varianti kasutama
print("Cinamoni tänane kinokava: ")
aeg_film = {}
for rida in kavarida:
    #print(rida)
    kellaaeg = rida.find('div', class_="schedule__time")
    film = rida.find('div', class_="schedule__film__name")
    aeg_film[kellaaeg.text.strip()] = film.text.strip()
for el in aeg_film:
    print(el + " : " + aeg_film[el])
#print(aeg_film)

#filmid_hulk = set()
#for film in filmid:
#    filmid_hulk.add(film.text.strip())

#print(filmid_hulk)
#print(len(filmid_hulk))
#print(filmide_arv)
    
    
    
    


# otsime lingi, mille sisu on Kinokava ja siis võtame selle href-i väärtuse ka
#for link in links:
#    if "Kinokava" in link.text:
#        print(link)
#        print(link.attrs['href'])


        
