
# Lenguaje          : Python
# Version           : 1.0
# Autor:            : Fernando Durán Torres

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from lxml import html 
import requests
import re
import datetime
import socket

def main():

    testConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    testConn.settimeout(5)
    try:
        testConn.connect(('www.google.com', 80))
    except (socket.gaierror, socket.timeout):
        print("Lo siento, pero no tienes internet. Comprueba tu conexión.")
    else:
        lecturaid()
        testConn.close()




def lecturaid():

    urltaxt = "https://weather.com/es-ES/tiempo/hoy/l/36.51,-4.88?par=google&temp=c"
    xmlpath(urltaxt)



def xmlpath(urltaxt):
    # URL de la web XML 
    page = requests.get(urltaxt) 
      
    # Parcheando URL 
    tree = html.fromstring(page.content) 
      
    # Extralyendo Xpath

    Tiempo = str(tree.xpath('/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/span/text()'))

    Tiempo = re.sub("\D", "", Tiempo)

   #Muestra por pantalla lo datos repilados 
    print("Temperatura: ", Tiempo)



if __name__ == "__main__":
    main()
