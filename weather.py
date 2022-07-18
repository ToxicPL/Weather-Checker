from requests import get
from json import loads
from terminaltables import AsciiTable

CITIES_LIST = ['Katowice', 'Kraków', 'Rzeszów', 'Warszawa']


def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [['Miasto', 'Godzina pomiaru', 'Temperatura', 'Ciśnienie']]

    for row in loads(response.text):
        if row['stacja'] in CITIES_LIST:
            rows.append([row['stacja'], row['godzina_pomiaru'], row['temperatura'], row['cisnienie']])
    table = AsciiTable(rows)
    print(table.table)


if __name__ == '__main__':
    print("Weather checker")
    main()
