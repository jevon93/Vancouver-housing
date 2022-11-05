# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

f = open('redata.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f)  
header = ['Beds', 'Baths', 'Price', 'StreetAddress', 'Area']
writer.writerow(header)

for pagenumber in range(262):
    URL = "https://www.remax.ca/bc/vancouver-real-estate?pageNumber=%d" % (pagenumber)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    job_elements = results.find_all("div", class_="listing-card_root__UG576 search-gallery_galleryCardRoot__7HbLb")

    for job_element in job_elements:
        price_element = job_element.find("h2",class_="listing-card_price__sL9TT")
        price_element = price_element.text.strip()
        price_element = price_element.replace(',','')
        price_element = price_element.replace('$','')
        
        property_element = job_element.find(class_="property-details_detailsWrapper__oDnwZ")
        property_elementy = property_element.text.strip()
        
        beds_element = property_elementy[:property_elementy.index("bed")]
        baths_element = property_elementy[property_elementy.index("bed")+3:property_elementy.index("bath")]
        address_element = job_element.find(class_="listing-address_root__PP_Ky listing-card_address___bLLz")
        
        street_element = address_element.text.strip()
        area_element = address_element.text.strip()
        
        street_element = street_element[:street_element.index(",")]
        area_element = area_element[area_element.index(","):]
        area_element = area_element.split(',')[1]
        
        data = [beds_element,baths_element,price_element, street_element, area_element.strip()]
        writer.writerow(data)

f.close()

"""
Spyder Editor

This is a temporary script file.
"""

