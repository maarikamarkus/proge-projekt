from bs4 import BeautifulSoup
import requests
import re

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



apollo_src = requests.get("https://www.apollokino.ee/?TheatreArea=1014&SetHome=1").text
apollo_aeg_film = apollo_aeg_film(apollo_src)
print('\n')
lounakeskus_src = requests.get("https://www.apollokino.ee/?TheatreArea=1011&SetHome=1").text
lounakeskus_aeg_film = lounakeskus_aeg_film(lounakeskus_src)


