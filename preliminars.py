# Aviso, esta cosa será borrada despues de usarse. 
import os
import requests as r
import zipfile

url_base = 'download'

def descarga(url, save_path, filename):
    html = r.get(url)
    with open(save_path + '\\' + filename) as download:
        download.write(html.content)

def extrae(extract_path: str, save_path: str, filename:str ):
    try:
        with zipfile.ZipFile(extract_path, 'r') as data:
            data.extractall(save_path + "\\"+ filename)
    except:
        print('Algo Fallo')



def preliminares(options: dict):
    if not os.path.exists(url_base + '\\Estados'):
        os.mkdir(url_base + '\\Estados')
        if not os.path.exists(url_base + '\\Mexico.zip'):
            if options['descarga'] == 'Si':
                url1 = "https://www.inegi.org.mx/contenidos/productos/prod_serv"
                url2 = "/contenidos/espanol/bvinegi/productos/geografia/marcogeo/794551067314_s.zip"
                Mexico = url1 + url2
                descarga(Mexico,'input', 'Mexico.zip')
        extrae(url_base + "\\Mexico.zip", url_base, "Estados")
    try:
        os.rename('download\\Estados\\mg_2023_integrado.zip','download\\REPMEX.zip')
    except: 
        print('El archivo esta en su lugar')


