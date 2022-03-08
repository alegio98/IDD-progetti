#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-


import bs4, requests , webbrowser , re

LINK = 'https://www.ording.roma.it/l-ordine/ordine/albo-iscritti/singolo-iscritto?matricola=19820'
response = requests.get(LINK)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser') #salva la pagina che è di tipo html.parser come file di testo , salvata in soup

nome = soup.find('h1',{'class':'alboNome'})
caratt_id = nome.text.split()

print("NOME = "+caratt_id[2])
print("COGNOME = "+ caratt_id[1])   #ok nome e cognome sistemati


tuttiIp= soup.find_all('p', {'class':'alboDati'})    #.find_next('span')
#citta=cittaNatale.find_next('span')

span= tuttiIp[0].find_all('span')

citta=span[0]
DataNascita = span[1]
print('CITTA = '+citta.text)
print('DATA = '+ DataNascita.text)

matricola= tuttiIp[1].find_all('span')
mat= matricola[0]
sezione= matricola[1]
print('MATRICOLA = '+mat.text)
print('SEZIONE = '+sezione.text)

annoEDS = tuttiIp[3].find_all('span')
anno=annoEDS[0]
print('ANNO ESAME DI STATO = '+anno.text)

luogoEDS=tuttiIp[4].find_all('span')
luogo=luogoEDS[0]
print('LUOGO ESAME DI STATO = '+luogo.text)

settore= tuttiIp[5].find_all('span')
sett= settore[0]
print('SETTORE = '+sett.text)

specializzazione=tuttiIp[6].find_all('span')
spec=specializzazione[0]
print('SPECIALIZZAZIONE = '+spec.text)

#in questo caso tutto va bene ma la struttura non è per tutte le pagine la stessa ...

text = 'Residenza'
gfg = soup.find_all(lambda tag: tag.name == "p" and text in tag.text)  #non so perche ma mi stampa prima tutti i p e poi quello che cerco io
iscrizione=gfg[1].find_all('span')
print(iscrizione)

#city=gfg[1].find_all('span')
#print(city[0].text) #cittaNatale
#print(city[1].text) #annoNascita
