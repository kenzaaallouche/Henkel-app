import os
import requests
from zipfile import ZipFile
from selenium import webdriver



# Ajouter le répertoire du pilote à la variable d'environnement PATH
driver_path = os.path.join('msedgedriver.exe')
os.environ['PATH'] += os.pathsep + os.path.dirname(driver_path)

# Démarrer le navigateur Edge
driver = webdriver.Edge(executable_path=driver_path)

# Exemple d'utilisation : naviguer vers une URL
driver.get("http://158.69.241.112/SalesBuzzBO/ReportManager/Default.aspx")

# Fermer le navigateur
driver.quit()


