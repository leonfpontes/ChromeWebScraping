#Imports
from selenium import webdriver

#Methods
def openChrome():
    navegador = webdriver.Chrome()
    navegador.get('https://www.google.com.br')

#Main
if __name__ == '__main__':
    openChrome()