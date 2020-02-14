import requests
from bs4 import BeautifulSoup

def get_html(url):
    result = requests.get(url)
    return result.text

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    h2 = soup.find('h1',{'class':'b-topic__title'})  #Заголовоу
    h1 = soup.find('div', {'class':'b-text clearfix js-topic__text'})
    h4 = soup.find('p',{})
    print(h4)
    h3 = 'Заголовок статьи:\n'+h2.text+'\n' + 'Статья:\n' + h1.text+'\n'
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