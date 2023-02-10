import requests
import random
from bs4 import BeautifulSoup
import os
def download(url, filename):
    file = requests.get(url)
    filec = open(filename, 'wb')
    filec.write(file.content)
    filec.close()
    return filename
def uploadFile(filename, proxy=""):
    infoRGCDL = requests.session()
    print('Iniciando sesion')
    logindata = {"username":"techdev","password":"@A1a2a3mo"}
    login = infoRGCDL.post("https://rcta.unah.edu.cu/index.php/RGCDL/login/signIn",data=logindata,allow_redirects=True,stream=True,proxies=dict(http=proxy,https=proxy))
    if "Cerrar sesión" in login.text:
    	print("**SESIÓN INICIADA**")
    	try:
    		data = {"articleId":1650,"from":"","title[es_ES]":random.randint(100000,999999),"creator[es_ES]":"TechDev","subject[es_ES]":"","type":"Texto fuente","typeOther[es_ES]":"","description[es_ES]":"Subido por TechDev","publisher[es_ES]":"","sponsor[es_ES]":"TechDev","dateCreated":"","source[es_ES]":"","language":"es"}
    		print("Datos creados")
    	except:
    		print("No se pudo crear los datos necesarios")
    	try:
    		files = {"uploadSuppFile":open(filename,"rb")}
    		
    		print("Archivo importado")
    	except:
    		print("No se pudo importar el archivo")
    	upFile = infoRGCDL.post("https://rcta.unah.edu.cu/index.php/RGCDL/author/saveSuppFile?path=",data=data,files=files,allow_redirects=True,stream=True,proxies=dict(http=proxy,https=proxy))
    	getLink = infoRGCDL.get("https://rcta.unah.edu.cu/index.php/RGCDL/author/submission/1650",proxies=dict(http=proxy,https=proxy))
    	soup = BeautifulSoup(getLink.text, "html.parser")
    	entradas = soup.find_all('a',{'class':'file'})
    	regex1 = str(entradas).split(",")
    	regex2 = regex1[int(len(regex1)) - 1]
    	regex3 = regex2.replace("]","")
    	regex4 = regex3.split("-")[1]
    	url = str("https://rcta.unah.edu.cu/index.php/RGCDL/author/downloadFile/1650/"+regex4)
    	print(url)
url = input("URL: ")
name = input("NAME: ")
uploadFile(download(url, name))