#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-

import bs4 , requests , webbrowser, re

LINK_INGEGNERI='https://www.ording.roma.it/l-ordine/ordine/albo-iscritti/risultati-ricerca-iscritti?Cognome=A&Nome=&Matricola=&Sezione='
response = requests.get(LINK_INGEGNERI)  #la funzione requests manda una richiesta di tipo get alla pagina LINK e il sito risponderà alla richiesta e ci invierà la pagina , la salviamo nel variabile response
response.raise_for_status()  #verifica se ci sono errori
soup = bs4.BeautifulSoup(response.text, 'html.parser') #salva la pagina che è di tipo html.parser come file di testo , salvata in soup

lista_ingegneri=soup.find_all('p',{'class':'listIscritti'})

link_ing=[] #lista link ingegneri

for a in lista_ingegneri :
    singolo_A = a.find('a')
    link_singolo= str(singolo_A.get('href'))
    link_ing.append(link_singolo)

nomiIngegneri=[]
cognomeIngegneri=[]
CittaIngegneri=[]
DataNascitaIngegneri=[]
MatricolaIngegneri =[]
AnnoIscrizioneIngegneri=[]
AnnoEsameIngegneri=[]
LuogoEsameStatoIngegneri=[]
SettoreIngegneri=[]
SpecialzzazioneIngegneri=[]
ResidenzaIngegneri=[]

PRE_LINK='https://www.ording.roma.it/'

for link in link_ing[0:1000]:

    responseING= requests.get(PRE_LINK+link)
    responseING.raise_for_status()
    soupING = bs4.BeautifulSoup(responseING.text,'html.parser')

    nome = soupING.find('h1',{'class':'alboNome'})
    caratt_id = nome.text.split()
    nomeIng= caratt_id[2]
    cognomeIng=caratt_id[1]
    nomiIngegneri.append(nomeIng)
    cognomeIngegneri.append(cognomeIng)

#VECCHIO METODO meno preciso
    #tuttiIp= soupING.find_all('p', {'class':'alboDati'})
    #nascitaSpan= tuttiIp[0].find_all('span')
    #cittaNascita=nascitaSpan[0]
    #dataNascita = nascitaSpan[1]
    #CittaIngegneri.append(cittaNascita.text)
    #DataNascitaIngegneri.append(dataNascita.text)

    text_nascita='Nato/a'
    p_nascita= soupING.find_all(lambda tag: tag.name == "p" and text_nascita in tag.text)
    span_nascita=p_nascita[1].find_all('span')
    CittaIngegneri.append(span_nascita[0].text)
    DataNascitaIngegneri.append(span_nascita[1].text)

    text_matricola='di iscrizione'
    p_matricola=soupING.find_all(lambda tag: tag.name == "p" and text_matricola in tag.text)
    span_matricola=p_matricola[1].find_all('span')
    MatricolaIngegneri.append(span_matricola[0].text)

    text_dataOrdine="iscrizione all'Ordine degli Ingegneri"
    p_dataOrdine=soupING.find_all(lambda tag: tag.name == "p" and text_dataOrdine in tag.text)
    span_dataOrdine=p_dataOrdine[1].find_all('span')
    AnnoIscrizioneIngegneri.append(span_dataOrdine[0].text)

    text_annoEsame = 'Anno esame di Stato'
    p_annoEsame=soupING.find_all(lambda tag: tag.name == "p" and text_annoEsame in tag.text)
    span_annoEsame=p_annoEsame[1].find_all('span')
    AnnoEsameIngegneri.append(span_annoEsame[0].text)

    text_luogoEsame= 'Luogo esame di Stato'
    p_luogoEsame=soupING.find_all(lambda tag: tag.name =='p' and text_luogoEsame in tag.text)
    span_luogoEsame = p_luogoEsame[1].find_all('span')
    LuogoEsameStatoIngegneri.append(span_luogoEsame[0].text)

    text_Settore='Settore'
    p_settore=soupING.find_all(lambda tag: tag.name =='p' and text_Settore in tag.text)
#MESSO PERCHE IN ALCUNI CASI POTREBBE NON ESSERCI UN VALORE PER IL SETTORE QUINDI HO DECISO DI METTERE IL VALORE NULL
    try:
        span_settore= p_settore[1].find_all('span')
        SettoreIngegneri.append(span_settore[0].text)
    except:
        SettoreIngegneri.append('NULL')

    text_spec='Specializzazione'
    p_spec=soupING.find_all(lambda tag: tag.name =='p' and text_spec in tag.text)
    span_spec=p_spec[1].find_all('span')
    SpecialzzazioneIngegneri.append(span_spec[0].text)

import pandas as pd
import numpy as np

data = {
        'Nome':  nomiIngegneri ,
        'Cognome':cognomeIngegneri ,
        'Citta': CittaIngegneri ,
        'Matricola':MatricolaIngegneri,
        'Settore': SettoreIngegneri,
        'Specializzazione': SpecialzzazioneIngegneri,
        'Anno Iscrizione':AnnoIscrizioneIngegneri,
        'Anno Esame Stato':AnnoEsameIngegneri,
        'Luogo Esame Stato':LuogoEsameStatoIngegneri,
         }

df = pd.DataFrame(data)
pd.set_option('display.expand_frame_repr', False)
#print(df)


#CREO IL FILE CSV e poi tramite il notebook grafico i dati

df.to_csv('ingegneri.csv', index=False)
