import requests
import bs4
import time
import random
import os
import dateparser
import re


######################################################
# CHANGE START URL FOR SPECIFIED SEARCH
#
data_file = "dane-vw-all.csv"
search_url = "https://www.otomoto.pl/osobowe/volkswagen/passat/od-2010/"
######################################################

def load_db():
    lista = []
    if os.path.isfile(data_file):
        with open(data_file) as fd:
            for l in fd:
                items = l.strip().split("\t")
                if items[0].isdigit():
                    lista.append(int(items[0].strip()))
    return lista


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def clear_text(text):
    """Generic function for clean text"""
    return text.replace("\n","").replace("\r","").replace(" ","")

def get_value_from_param(tag):
    """Get text value from html tag"""
    try:
        return tag.text.strip()
    except:
        return None


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


announces = load_db()


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0',
}

result = requests.get(search_url, headers=headers)
html_data = bs4.BeautifulSoup(result.text, features='lxml')
#print(html_data)
max_page = int(html_data.select('.page')[-1].text)
print("Liczba stron dla wynikow=",max_page)


header = "ID;Data;Link;Nazwa;Cena;Lokalizacja;Rocznik;Przebieg;Paliwo;Nadwozie;VAT;Do negocjacji;" \
         "Oferta od;Marka pojazdu;Model pojazdu;Wersja;Kategoria;Napęd;Moc;Skrzynia biegów;Typ;Liczba drzwi;\
         Liczba miejsc;Kolor;Perłowy;" \
         "Kraj pochodzenia;Pierwsza rejestracja;Zarejestrowany w Polsce;Bezwypadkowy;Serwisowany w ASO;Stan;" \
         "Pierwszy właściciel;Metalik;Możliwość finansowania;VIN;Pojemność skokowa;Wyposażenie"

if not os.path.exists(data_file):
    with open(data_file, "at") as fd:
            line = "\t".join(header.strip().split(";"))
            fd.write(line)
            fd.write("\n")

counter, total = 0, 1
for index in range(1, max_page+1):
    url = f"{search_url}&page={index}"

    result = None
    counter = 10
    while counter > 0:
        try:
            result = requests.get(url, headers=headers)
            break
        except:
            print("Error: ", url_detail)
            time.sleep(5)
            counter -= 1

    if result == None:
        pass

    html_data = bs4.BeautifulSoup(result.text, features='lxml')


    items =  html_data.select('article.offer-item')
    for item in items:
        counter+=1

        offer_id =  item.attrs["data-ad-id"]
        if int(offer_id) in announces:
            print(f"Ogłoszenie {offer_id} już jest w pliku")
            continue

        url_detail = item.attrs["data-href"]

        title = item.find('a', class_='offer-title__link').text.strip()

        price = clear_text(item.find('span', class_='offer-price__number').text.strip())

        result = None
        counter=10
        while counter>0:
            try:
                result = requests.get(url_detail, headers=headers)
                break
            except:
                print("Error: ",url_detail)
                time.sleep(5)
                counter -= 1

        if result==None:
            pass

        details_data = bs4.BeautifulSoup(result.text, features='lxml')
        params = details_data.find_all('span', class_='offer-main-params__item')

        doa = None
        try:
            txt = result.text;
            i = txt.find("<span class=\"offer-meta__item\">")
            if i:
                txt = txt[i:]
                i = txt.find("</span>")
                if i:
                    txt = txt[0:i].strip()
                    txt = cleanhtml(txt)
                    txt = str(dateparser.parse(txt.strip(), languages=['pl']))
                    doa = txt
        except:
            doa = None

        try:
            yom = get_value_from_param(params[0])
        except:
            yom = None

        try:
            mileage = get_value_from_param(params[1])
        except:
            mileage = None

        try:
            fuel = get_value_from_param(params[2])
        except:
            fuel = None

        try:
            chasis = get_value_from_param(params[3])
        except:
            chasis

        try:
            location = details_data.find('span', class_='seller-box__seller-address__label').text.strip()
        except:
            location = None


        parameters = dict()
        param_data = details_data.find_all('li', class_='offer-params__item')
        for par in param_data:
            elems = [remove_html_tags(str(x)).strip() for x in par.contents if remove_html_tags(str(x)).strip()!=""]
            parameters[elems[0]] = elems[1]

        try:
            items = details_data.find_all('li', class_='offer-features__item')
            list = [item.text.strip().upper() for item in items]
            features = "|".join(list)
        except:
            features = None

        fvat = "NIE"
        negotiations = "NIE"
        try:
            s = details_data.find('span', class_="offer-price__details").text.strip().lower()
            if "faktura vat" in s:
                fvat = "TAK"
            if "do negocjacji" in s:
                negotiations = "TAK"
        except:
            pass

        data_row = []
        print("Lp:",total)
        print("ID:",offer_id); data_row.append(offer_id);
        print("Data:", doa); data_row.append(doa);
        print("Link:", url_detail); data_row.append(url_detail);
        print("Nazwa:",title); data_row.append(title);
        print("Cena:",price); data_row.append(price);
        print("Lokalizacja:", location); data_row.append(location)

        print("Rocznik:",yom); data_row.append(yom);
        print("Przebieg:",mileage); data_row.append(mileage);
        print("Paliwo:",fuel); data_row.append(fuel);
        print("Nadwozie:",chasis); data_row.append(chasis);
        print("VAT:",fvat); data_row.append(fvat);
        print("Do negocjacji:",negotiations); data_row.append(negotiations);

        data_row.append(parameters.get("Oferta od","?"))
        data_row.append(parameters.get("Marka pojazdu","?"))
        data_row.append(parameters.get("Model pojazdu","?"))
        data_row.append(parameters.get("Wersja","?"))
        data_row.append(parameters.get("Kategoria","?"))
        data_row.append(parameters.get("Napęd","?"))
        data_row.append(parameters.get("Moc","?"))
        data_row.append(parameters.get("Skrzynia biegów","?"))
        data_row.append(parameters.get("Typ","?"))
        data_row.append(parameters.get("Liczba drzwi",-1))
        data_row.append(parameters.get("Liczba miejsc",-1))
        data_row.append(parameters.get("Kolor","?"))
        data_row.append(parameters.get("Perłowy","?"))
        data_row.append(parameters.get("Kraj pochodzenia","?"))
        data_row.append(parameters.get("Pierwsza rejestracja","?"))
        data_row.append(parameters.get("Zarejestrowany w Polsce","?"))
        data_row.append(parameters.get("Bezwypadkowy","?"))
        data_row.append(parameters.get("Serwisowany w ASO","?"))
        data_row.append(parameters.get("Stan","?"))
        data_row.append(parameters.get("Pierwszy właściciel","?"))
        data_row.append(parameters.get("Metalik","?"))
        data_row.append(parameters.get("Możliwość finansowania","?"))
        data_row.append(parameters.get("VIN","?"))
        data_row.append(parameters.get("Pojemność skokowa","?"))

        total += 1
        print("Wyposażenie:", features); data_row.append(features);

        print("-"*30)

        with open(data_file,"at") as fd:
            line = "\t".join([str(x) for x in data_row])
            fd.write(line)
            fd.write("\n")

        time.sleep( random.randint(10,100) /1000.0)

