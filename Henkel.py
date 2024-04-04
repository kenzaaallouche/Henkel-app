from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# Chemin vers le Microsoft WebDriver. Assurez-vous de remplacer le chemin par celui où vous avez téléchargé le pilote.
driver_path = r'C:/Users/deyha/Desktop/App Scrapping/msedgedriver.exe'

# Options du navigateur Edge
#edge_options = webdriver.EdgeOptions()

# Initialisation du navigateur Edge avec les options
driver = webdriver.Edge(executable_path=r'C:/Users/deyha/Desktop/App Scrapping/msedgedriver.exe')
driver.get("http://158.69.241.112/SalesBuzzBO/ReportManager/Default.aspx")
