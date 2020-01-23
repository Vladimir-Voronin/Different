import requests
from bs4 import BeautifulSoup
import csv
import xlwt
import time


def insoup():
    file = open('url.txt', 'r').read()
    soup = BeautifulSoup(file, 'lxml')
    film_list = soup.find('div', {'class': 'profileFilmsList'})
    items = film_list.find_all('div', {'class': ['item', 'item even']})
    film_list = []
    
    for item in items:
        movie_desc = item.find('div', {'class': 'nameRus'}).find('a').text
        movie_vote = item.find('div', {'class': 'vote'}).text
        name_list = [movie_desc,movie_vote]
        film_list.append(name_list)
        print(movie_desc + ': ' + str(movie_vote))

    print(film_list)
    return film_list

        
def csv_func(listfilms):   #Dont work
    FILENAME = "users.csv"
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file, delimiter = ',')
        writer.writerows(listfilms)

def excel_func(listfilms):
    exfile = xlwt.Workbook(encoding="utf-8")
    exbook = exfile.add_sheet('Films')
    n = 0
    for i in listfilms:
        exbook.write(n,0,listfilms[n][0])
        exbook.write(n,1,listfilms[n][1])
        n += 1
    exfile.save('films.xls')

def main():
    timelast = time.time()
    film_list = insoup()
    excel_func(film_list)
    timenow = time.time() - timelast
    print('Time: ' + str(timenow))


if __name__ == '__main__':
    main()
