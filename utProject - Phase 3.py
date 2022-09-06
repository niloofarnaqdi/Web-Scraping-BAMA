from requests import Session
from bs4 import BeautifulSoup
import pandas as pd

ses = Session()
user = 610399202
ramz = 70238155249809984818
capt = 12345

datalist = []

for x in range (500):
    ads = []
    # Company, Car, Tream, Kilometer, Year, Price
    url = 'http://utproject.ir/bp/Cars/page{}.php'.format(x)
    page = ses.post('http://utproject.ir/bp/login.php', data = {"username":str(user), "password":str(ramz),"captcha":capt})
    index = ses.get (url)
    index.encoding = 'utf8'

    soup = BeautifulSoup (index.content, 'html.parser')
    ads = soup.find_all ('li', class_ = 'car-list-item-li list-data-main')
    for ad in ads:
        agahi = dict()

        #Release Date
        year = int(ad.find ('span', itemprop = "releaseDate").text)

        #Company, Car and Tream
        main = str(ad.find ('a', itemprop="url")).split('>')[0]
        dat = str(main).split('-')
        dat.remove ('<a href="https://bama.ir/car/detail')
        dat.remove ('{}" itemprop="url"'.format(year))

        #Price
        price1 = ad.find ('p', itemprop = "price")
        price2 = ad.find ('span', itemprop="price")
        if price1 == None:
            pr = str(price2).split('"')
            price = (pr[1])
        elif price2 == None:
            pr = str(price1).split('"')
            price = (pr[3])

        #Kilometer
        karkard = ad.find ('div', class_='car-func-details')
        w = str (karkard.text).split('|')
        fin = []
        for el in w:
            fin.append (el.strip())
        work = fin[0].split()
        work.remove ('کارکرد')  
        work = str(work[0])

        kar = ""
        for _ in work:
            if _ != ',':
                kar += _

        agahi['company'] = dat[1]
        agahi['car'] = dat[2]
        agahi['tream'] = ('-'.join(dat[3:]) if len(dat)>=4 else "None")
        agahi['year'] = year
        agahi['price'] = price
        agahi['kilometer'] = 0 if work in [0, '-', 'صفر'] else int(kar)

        datalist.append (agahi)
        
#Output: datalist