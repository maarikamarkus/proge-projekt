# programmeerimise aine projekt
# idee luua programm, mis leiab kõige odavama kinokülastuse variandi tartus
# selleks kasutame lisandmoodulit beautifulsoup, mis tuleb eraldi endale lisada
# samuti tuleb lisanda requests -- tools > manage packages.. > otsingusse requests > install
# ja samamoodi lisada ka lxml
# esialgne abistav info: https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python
# sellele moodulile tuleb ise URL-e sööta, siis teeb neist soup-objecti

# https://www.youtube.com/watch?v=ng2o98k983k -- hea video beautifulsoupi kohta

# cinamon
# class = "schedule_film_name" - kinokavas oleva filmi class
# class = "pageSeatPlan_ticketTypes--standard" -- tavaline pilet
# class = "pageSeatPlan_ticketTypes--love" -- loveseat pilet

# kõigepealt proovime cinamoni lehelt vajaliku info kätte saada

from bs4 import BeautifulSoup
import requests

# request.get() abil saame veebilehe kätte
source = requests.get("https://cinamonkino.com/tasku/").text

# BeautifulSoup annab meile selle lehe html koodi
soup = BeautifulSoup(source, 'lxml')

# soup.prettify() teeb html koodile õiged taanded
print(soup.prettify())
