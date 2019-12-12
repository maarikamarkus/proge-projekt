from bs4 import BeautifulSoup
import requests

def apollo_aeg_film(apollo_src):
    apollo_kinokava = BeautifulSoup(apollo_src, 'lxml')
    apollo_kavarida = apollo_kinokava.find_all('div', class_="panel-body")

    print("Kino Apollo tänane kinokava on: ")
    apollo_aeg_film = {}
    for apollo_rida in apollo_kavarida:
        #print(apollo_rida)
        apollo_film = apollo_rida.find('h2', class_="list-item-desc-title")
        apollo_filminimi = (apollo_film.find("a")).text.strip()
        #print(apollo_film)
        print(apollo_filminimi)
        apollo_kellaaeg = apollo_rida.find("div", class_="btn-group")
        apollo_kell = (apollo_kellaaeg.find("span")).text.strip()
        #print (apollo_kellaaeg)
        print(apollo_kell)
        #apollo_aeg_film[apollo_kellaaeg.text.strip()] = apollo_film.text.strip()
    #for apollo_el in apollo_aeg_film:
        #print(apollo_el + " : " + apollo_aeg_film[apollo_el])
    print("\n")


apollo_src = requests.get("https://www.apollokino.ee/?TheatreArea=1014&SetHome=1").text
print(apollo_aeg_film(apollo_src))

#apollo_kavarida = apollo_kinokava.find_all('h2', class_="list-item-desc-title")

#print("Kino Apollo tänane kinokava on: ")
#for apollo_rida in apollo_kavarida:
#    apollo_film = apollo_rida.find('a', href = True).text.strip()
#    print(apollo_film)
#print("\n")
