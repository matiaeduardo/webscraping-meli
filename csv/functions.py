from bs4 import BeautifulSoup as bs
import requests
from lxml import etree

def todosproductos(producto):
    t_lista=[]
    u_lista=[]
    p_lista=[]
    sig='https://listado.mercadolibre.com.ar/'+ producto
    while True:
            r=requests.get(sig)
            if r.status_code==200:
                soup=bs(r.content,'html.parser')
                #nombres
                titles=soup.find_all('h2',attrs={'class':'ui-search-item__title shops__item-title'})
                titles=[i.text for i in titles]
                t_lista.extend(titles)
                #urls
                urls=soup.find_all('a',attrs={'class':'ui-search-item__group__element shops__items-group-details ui-search-link'})
                urls=[i.get('href') for i in urls]
                u_lista.extend(urls)
                #precios
                dom=etree.HTML(str(soup))
                precios=dom.xpath("//li[@class='ui-search-layout__item shops__layout-item']//div[@class='ui-search-price__second-line shops__price-second-line']/span/span[2]/span[2]")
                precios=[i.text for i in precios]
                p_lista.extend(precios)
                #indices
                indice=soup.find('span',attrs={'class':'andes-pagination__link'}).text
                indice=int(indice)
                indice2=soup.find('li',attrs={'class':'andes-pagination__page-count'})
                indice2=int(indice2.text.split(' ')[1])
            else:
                break
            print(indice,indice2)
            if indice==indice2:
                break
            sig=dom.xpath("//div[@class='ui-search-pagination shops__pagination-content']/ul/li[contains(@class,'--next')]/a")[0].get('href')    
    return t_lista,u_lista,p_lista

def limite_producto(producto,limite):
    t_lista=[]
    u_lista=[]
    p_lista=[]
    sig='https://listado.mercadolibre.com.ar/'+ producto
    while True:
            r=requests.get(sig)
            if r.status_code==200:
                soup=bs(r.content,'html.parser')
                #nombres
                titles=soup.find_all('h2',attrs={'class':'ui-search-item__title shops__item-title'})
                titles=[i.text for i in titles]
                t_lista.extend(titles)
                #urls
                urls=soup.find_all('a',attrs={'class':'ui-search-item__group__element shops__items-group-details ui-search-link'})
                urls=[i.get('href') for i in urls]
                u_lista.extend(urls)
                #precios
                dom=etree.HTML(str(soup))
                precios=dom.xpath("//li[@class='ui-search-layout__item shops__layout-item']//div[@class='ui-search-price__second-line shops__price-second-line']/span/span[2]/span[2]")
                precios=[i.text for i in precios]
                p_lista.extend(precios)
                #indices
                indice=soup.find('span',attrs={'class':'andes-pagination__link'}).text
                indice=int(indice)
                indice2=soup.find('li',attrs={'class':'andes-pagination__page-count'})
                indice2=int(indice2.text.split(' ')[1])
            else:
                break
            print(indice,indice2)
            if len(t_lista)>=int(limite):
                return t_lista[:limite],u_lista[:limite],p_lista[:limite]
            if indice==indice2:
                break
            sig=dom.xpath("//div[@class='ui-search-pagination shops__pagination-content']/ul/li[contains(@class,'--next')]/a")[0].get('href')    
    return t_lista,u_lista,p_lista