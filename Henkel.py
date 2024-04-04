import os
import requests
from zipfile import ZipFile
from selenium import webdriver

# URL du pilote Microsoft Edge sur GitHub
driver_url = 'https://github.com/kenzaaallouche/Henkel-app/blob/158855ef4d6a0f252ac4fc14cee5ee7db66c5f47/edgedriver_win64%20(3).zip'

# Répertoire de téléchargement
download_dir = './drivers'

# Télécharger le pilote Edge depuis GitHub
response = requests.get(driver_url)
zip_file_path = os.path.join('msedgedriver.zip')
with open(zip_file_path, 'wb') as f:
    f.write(response.content)

# Extraire le pilote de l'archive ZIP
with ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(download_dir)

# Ajouter le répertoire du pilote à la variable d'environnement PATH
driver_path = os.path.join(download_dir, 'msedgedriver.exe')
os.environ['PATH'] += os.pathsep + os.path.dirname(driver_path)

# Démarrer le navigateur Edge
driver = webdriver.Edge(executable_path=driver_path)

# Exemple d'utilisation : naviguer vers une URL
driver.get("http://158.69.241.112/SalesBuzzBO/ReportManager/Default.aspx")

# Fermer le navigateur
driver.quit()


