import os

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import tkinter as tk

class TestKetest():
  def setup_method(self, method):
        EDGE_DRIVER_PATH = r'msedgedriver.exe'

        # Options du navigateur Edge
        edge_options = EdgeOptions()

        # Spécifiez le chemin de téléchargement
        prefs = {
            "download.default_directory": "C:\\Users\\deyha\\Desktop\\SCRAPPING",
            "download.default_filename": "nom_du_fichier.extension",
            "download.prompt_for_download": False,
        }

        # Configurez les options du navigateur Edge avec les préférences
        edge_options.set_capability("ms:edgeChromium", True)
        edge_options.add_experimental_option("prefs", prefs)
        edge_options.use_chromium = True
        #edge_options.add_argument("--headless")  # Activer le mode headless

        # Initialisation du navigateur Edge avec les options
        self.driver = Edge(executable_path=EDGE_DRIVER_PATH, options=edge_options)
    
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_ketest(self):
    # Test name: ketest
    # Step # | name | target | value
    # 1 | open | /SalesBuzzBO/ReportManager/Default.aspx | 
    self.driver.get("http://158.69.241.112/SalesBuzzBO/ReportManager/Default.aspx")
    # 2 | setWindowSize | 535x720 | 
    self.driver.set_window_size(535, 720)
    # 3 | click | id=TextUserName | 
    self.driver.find_element(By.ID, "TextUserName").click()
    # 4 | type | id=TextUserName | BO16K
    self.driver.find_element(By.ID, "TextUserName").send_keys("BO16K")
    # 5 | type | id=TextPassword | kenza1999
    self.driver.find_element(By.ID, "TextPassword").send_keys("kenza1999")
    # 6 | click | id=DropDownList1 | 
    self.driver.find_element(By.ID, "DropDownList1").click()
    # 7 | select | id=DropDownList1 | label=French
    dropdown = self.driver.find_element(By.ID, "DropDownList1")
    dropdown.find_element(By.XPATH, "//option[. = 'French']").click()
    # 8 | click | id=txtBusinessUnit | 
    self.driver.find_element(By.ID, "txtBusinessUnit").click()
    # 9 | type | id=txtBusinessUnit | 111101
    self.driver.find_element(By.ID, "txtBusinessUnit").send_keys("111101")
    # 10 | click | id=ButtonLogin | 
    self.driver.find_element(By.ID, "ButtonLogin").click()
    # 11 | click | css=#ReportsTreet31i > img | 
    self.driver.find_element(By.CSS_SELECTOR, "#ReportsTreet31i > img").click()
    # 12 | click | id=ContentPlaceHolder1_FiltersGridView_f186f1_0 | 
    self.driver.find_element(By.ID, "ContentPlaceHolder1_FiltersGridView_f186f1_0").click()
    # 13 | type | id=ContentPlaceHolder1_FiltersGridView_f186f1_0 | 21/03/2024
    self.driver.find_element(By.ID, "ContentPlaceHolder1_FiltersGridView_f186f1_0").send_keys("01/03/2024")
    # 14 | click | id=ContentPlaceHolder1_FiltersGridView_f186f2_1 | 
    self.driver.find_element(By.ID, "ContentPlaceHolder1_FiltersGridView_f186f2_1").click()
    # 15 | type | id=ContentPlaceHolder1_FiltersGridView_f186f2_1 | 21/03/2024
    self.driver.find_element(By.ID, "ContentPlaceHolder1_FiltersGridView_f186f2_1").send_keys("21/03/2024")
    # 16 | click | id=ContentPlaceHolder1_FiltersGridView_f186f21_32 | 
    self.driver.find_element(By.ID, "ContentPlaceHolder1_FiltersGridView_f186f21_32").click()
    # 17 | type | id=ContentPlaceHolder1_FiltersGridView_f186f21_32 | PS16F01
    self.driver.find_element(By.ID, "ContentPlaceHolder1_FiltersGridView_f186f21_32").send_keys("MM16F01")
    # 18 | type | id=ContentPlaceHolder1_FiltersGridView_f186f21_32 | PS16F01
    
    # 19 | click | id=ContentPlaceHolder1_FiltersGridView_f186f22_33 | 
    self.driver.find_element(By.ID, "ContentPlaceHolder1_FiltersGridView_f186f22_33").click()
    # 20 | type | id=ContentPlaceHolder1_FiltersGridView_f186f22_33 | PS16F01

    # 21 | type | id=ContentPlaceHolder1_FiltersGridView_f186f22_33 | PS16F01
    self.driver.find_element(By.ID, "ContentPlaceHolder1_FiltersGridView_f186f22_33").send_keys("WS16F02")
    # 22 | click | css=#ContentPlaceHolder1_Button1 > img | 
    self.vars["window_handles"] = self.driver.window_handles
    # 23 | selectWindow | handle=${win6385} | 
    self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_Button1 > img").click()
    # 24 | click | css=#CrystalReportViewer1_toptoolbar_export div | 
    #self.vars["win6385"] = self.wait_for_window(2000)
    # 25 | click | id=IconImg_Txt_iconMenu_icon_bobjid_1711201100952_dialog_combo | 
    #self.driver.switch_to.window(self.vars["win6385"])
    self.driver.switch_to.window(self.driver.window_handles[-1])
    # 26 | click | id=iconMenu_menu_bobjid_1711201100952_dialog_combo_span_text_bobjid_1711201100952_dialog_combo_it_14 | 
    self.driver.find_element(By.CSS_SELECTOR, "#CrystalReportViewer1_toptoolbar_export div").click()
    # 27 | click | css=body | 
    self.driver.find_element(By.XPATH, "//td/div/table/tbody/tr/td/table/tbody/tr/td[2]/div").click()
    self.driver.find_element(By.XPATH, "//tr[5]/td[2]/span").click()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.LINK_TEXT, "Exporter").click()
    print("fin exec")
    time.sleep(5)
    
def h():
    test_instance = TestKetest()

    # Appelez la méthode setup_method pour initialiser le pilote
    test_instance.setup_method(None)

    # Appelez la méthode test_ketest() sur cette instance
    test_instance.test_ketest()
    time.sleep(10)

    print("fin exec")
