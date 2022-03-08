#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-

#lavoro in singolo per ora per capire come approcciare alle singole aziende, facilmente poi posso applicare il medesimo
#approccio per estrarre dati da molte aziende.

import bs4, requests , webbrowser , re

LINK = 'https://www.value.today/company/amazon.com'
response = requests.get(LINK)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser') #salva la pagina che è di tipo html.parser come file di testo , salvata in soup

## NOME AZIENDA
nomeAzienda= soup.find('h1',{'class':'clearfix col-sm-12'})

## DELLA POSIZIONE MONDIALE
lastWRank= soup.find('div',{'class':'clearfix col-sm-6 field field--name-field-world-rank-jan072022 field--type-integer field--label-above'})
itemWR=lastWRank.find('div',{'class':'field--item'})

##ANNUAL REVENUE
annualRevenue= soup.find('div',{'class':'clearfix col-sm-12 field field--name-field-revenue-in-usd field--type-float field--label-inline'})
itemAR=annualRevenue.find('div',{'class':'field--item'})

#HEAD COUNTRY
hCountry= soup.find('div',{'class':'clearfix col-sm-12 field field--name-field-headquarters-of-company field--type-entity-reference field--label-inline'})
itemHCountry=hCountry.find('div',{'class':'field--item'})

#MAIN COMPANY BUSINESS i 4 affari aziendali principali di ogni azienda (di cosa si occupa)
compBusin= soup.find('div',{'class':'clearfix col-sm-12 field field--name-field-company-category-primary field--type-entity-reference field--label-inline'})
itemBusin=compBusin.find_all('div',{'class':'field--item'})
print("Main Company Business: ")
for i in itemBusin[0:4]:
    print(i.text)

##CEO
ceo = soup.find('div',{'class':'clearfix col-sm-12 field field--name-field-ceo field--type-entity-reference field--label-above'})
itemCeo=ceo.find('div',{'class':'field--item'})

##FOUNDERS
founders = soup.find('div',{'class':'clearfix col-sm-12 field field--name-field-founders field--type-entity-reference field--label-above'})
itemFounders=founders.find_all('div',{'class':'field--items'})
print('Founders :')
for i in itemFounders:
    print(i.text)

##FOUNDED YEAR
fYear= soup.find('div',{'class':'clearfix col-sm-12 field field--name-field-founded-year field--type-integer field--label-inline'})
itemfY=fYear.find('div',{'class':'field--item'})

##WEBSITE
website=soup.find('div',{'class':'clearfix col-sm-12 field field--name-field-company-website field--type-link field--label-above'})
itemWS=website.find('a')
hrefItemWS=str(itemWS.get('href'))



print("Nome : "+nomeAzienda.text)
print("World Rank : "+itemWR.text)
print("Annual Revenue : " +itemAR.text)
print("Headquarters Country : " +itemHCountry.text)
print('CEO : '+itemCeo.text)
print('Founded Year : '+itemfY.text)
print('Web Site : '+hrefItemWS)
