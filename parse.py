import requests
from bs4 import BeautifulSoup

def get_html(url):
    result = requests.get(url)
    return result.text
abc = ''
def get_data(html):
    global abc
    soup = BeautifulSoup(html,'lxml')
    h2 = soup.find('h1',{'class':'b-topic__title'})  #Заголовок
    h1 = soup.find('div', {'class':'b-text clearfix js-topic__text'})
    print(h2.text)
    for i in soup.find_all('p'):
        abc = abc + i.text
   # print(abc)
    h3 = 'Заголовок статьи:\n'+h2.text+'\n' + 'Статья:\n' + abc+'\n'
    #print(h3)
    f = open('text.txt','w',encoding='utf-8')
    f.write(h3)
    f.close()
    if f.closed == True:
        print('Записы выполнена!')

    else:
        print('Запись не выполнена!')

def main():
    html = get_html(input('Введите URL сайта Lenta.ru'))
    get_data(html)

if __name__ == '__main__':
    main()