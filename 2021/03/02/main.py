import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

soup = BeautifulSoup(requests.get(alba_url).text, 'html.parser')

company_links = [{'link': info['href']+'job/brand/', 'name': info.find('span', attrs={'class': 'company'}).get_text(
)} for info in soup.find_all('a', attrs={'class': 'goodsBox-info'}) if info['href'][0] != '/']
for company_link in company_links:
    file = open(f"{company_link['name']}.csv", mode='w')
    writer = csv.writer(file)
    writer.writerow(['place', 'title', 'time', 'pay', 'date'])
    company_soup = BeautifulSoup(requests.get(
        company_link['link']).text, 'html.parser')
    trs = company_soup.find_all('tr')
    for tr in trs:
        try:
            if tr['class'] == []:
                tds = tr.find_all('td')
                row = []
                for td in tds:
                    row.append(td.get_text())
                writer.writerow(row)
        except:
            pass

    # company_doc = requests.get(company_link).text
    # company_soup = BeautifulSoup(company_doc, 'html.parser')
    # company_soup.find('div', attrs={'id': 'NormalInfo'}).find_all()
