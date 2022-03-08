#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-

import bs4 , requests , webbrowser, re

for i in range(0,2):
    print('https://www.value.today/world/world-top-1000-companies?page='+str(i))  #tutte le pagine , processamento migliore uno alla volta

### sul prompt dei comandi dare questo per fare MERGE DEI FILE CSV ==> awk '(NR == 1) || (FNR > 1)' *.csv > bigfile.csv

LINK_AZIENDE='https://www.value.today/world/world-top-1000-companies?page=9'
response = requests.get(LINK_AZIENDE)  #la funzione requests manda una richiesta di tipo get alla pagina LINK e il sito risponderà alla richiesta e ci invierà la pagina , la salviamo nel variabile response
response.raise_for_status()            #verifica se ci sono errori
soup = bs4.BeautifulSoup(response.text, 'html.parser') #salva la pagina che è di tipo html.parser come file di testo , salvata in soup

lista_aziende= soup.find_all('h2',{'class':'field-content'})

link_aziende=[] #lista link aziende

for a in lista_aziende :
    singola_A = a.find('a')
    link_singola= str(singola_A.get('href'))
    link_aziende.append(link_singola)

nomiAziende=[]
rankPosizioniMondo=[]
entrateAnnuali=[]         #annual revenue
hCountryes=[]
mainBSS=[]
ceos=[]
region=[]
fYears=[]
wsites=[]


PRE_LINK='https://www.value.today'


for link in link_aziende:
    responseAZ= requests.get(PRE_LINK+link)
    responseAZ.raise_for_status()
    soupAZ = bs4.BeautifulSoup(responseAZ.text,'html.parser')

## NOME AZIENDA
    nomeAzienda= soupAZ.find('h1',{'class':'clearfix col-sm-12'})
    nomiAziende.append(nomeAzienda.text)

## RANK DELLA POSIZIONE MONDIALE
    lastWRank= soupAZ.find('div',{'class':'clearfix col-sm-6 field field--name-field-world-rank-jan072022 field--type-integer field--label-above'})
    try:
        itemWR=lastWRank.find('div',{'class':'field--item'})
        rankPosizioniMondo.append(itemWR.text)
    except:
        rankPosizioniMondo.append("NULL")

## ANNUAL REVENUE
    annualRevenue= soupAZ.find('div',{'class':'clearfix col-sm-12 field field--name-field-revenue-in-usd field--type-float field--label-inline'})
    try:
        itemAR=annualRevenue.find('div',{'class':'field--item'})
        entrateAnnuali.append(itemAR.text)
    except:
        entrateAnnuali.append('NULL')

## HEAD COUNTRY
    hCountry= soupAZ.find('div',{'class':'clearfix col-sm-12 field field--name-field-headquarters-of-company field--type-entity-reference field--label-inline'})
    itemHCountry=hCountry.find('div',{'class':'field--item'})
    hCountryes.append(itemHCountry.text)

## MAIN COMPANY BUSINESS i 4 affari aziendali principali di ogni azienda (di cosa si occupa)
    compBusin= soupAZ.find('div',{'class':'clearfix col-sm-12 field field--name-field-company-category-primary field--type-entity-reference field--label-inline'})
    itemBusin=compBusin.find_all('div',{'class':'field--item'})
    for i in itemBusin[0:1]:
        mainBSS.append(i.text)

## CEO
    ceo = soupAZ.find('div',{'class':'clearfix col-sm-12 field field--name-field-ceo field--type-entity-reference field--label-above'})
    try:
        itemCeo=ceo.find('div',{'class':'field--item'})
        ceos.append(itemCeo.text)
    except:
        ceos.append('NULL')

## WORLD SUB REGION
    wsRegion = soupAZ.find('div',{'class':'clearfix col-sm-12 field field--name-field-continental-sub-region field--type-entity-reference field--label-inline'})
    try:
        itemwsRegion=wsRegion.find('div',{'class':'field--item'})
        region.append(itemwsRegion.text)
    except:
        founD.append('NULL')


## FOUNDED YEAR
    fYear= soupAZ.find('div',{'class':'clearfix col-sm-12 field field--name-field-founded-year field--type-integer field--label-inline'})
    try:
        itemfY=fYear.find('div',{'class':'field--item'})
        fYears.append(itemfY.text)
    except:
        fYears.append("NULL")

## WEBSITE
    website=soupAZ.find('div',{'class':'clearfix col-sm-12 field field--name-field-company-website field--type-link field--label-above'})
    try:
        itemWS=website.find('a')
        hrefItemWS=str(itemWS.get('href'))
        wsites.append(hrefItemWS)
    except:
        wsites.append('NULL')


#print("World Rank : "+itemWR.text)
#print("Annual Revenue : " +itemAR.text)
#print("Headquarters Country : " +itemHCountry.text)
#print('CEO : '+itemCeo.text)


import pandas as pd
import numpy as np

data = {
        'Nome':  nomiAziende ,
        'Rank':rankPosizioniMondo ,
        'Sector':mainBSS,
        'Entry Annual': entrateAnnuali ,
        'Sector':mainBSS,
        'CEO':ceos,
        'Head Country':hCountryes,
        'Region':region,
        'WebSite': wsites
         }

df = pd.DataFrame(data)
pd.set_option('display.expand_frame_repr', False)
#print(df)


#CREO IL FILE CSV e poi tramite il notebook grafico i dati

df.to_csv('aziende9.csv', index=False)
