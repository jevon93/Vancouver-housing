# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

f = open('redata.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f)  
header = ['BedsBaths', 'Price', 'FullAddress']
writer.writerow(header)

for pagenumber in range(262):
    URL = "https://www.remax.ca/bc/vancouver-real-estate?pageNumber=%d" % (pagenumber)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="__next")

    job_elements = results.find_all("div", class_="listing-card_root__UG576 search-gallery_galleryCardRoot__7HbLb")

 

    for job_element in job_elements:
        price_element = job_element.find("h2",class_="listing-card_price__sL9TT")
        property_element = job_element.find(class_="property-details_detailsWrapper__oDnwZ")
        address_element = job_element.find(class_="listing-address_root__PP_Ky listing-card_address___bLLz")
        data = [property_element.text.strip(),price_element.text.strip(),address_element.text.strip()]
        writer.writerow(data)

        
f.close()   
"""
Spyder Editor

This is a temporary script file.
"""

