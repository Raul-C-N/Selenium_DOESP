# Generated by Selenium IDE
from lib2to3.pytree import Base
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import datetime


PATH = "C:\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
hoje = datetime.datetime.now()
dd = hoje.day
mm = hoje.month
aa = hoje.year
data = str(dd)+'/'+str(mm)+'/'+str(aa)

class TestDOESPSELENIUM():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(PATH)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dOESPSELENIUM(self):
    self.driver.get("http://www.imprensaoficial.com.br/#"+data) #colocar o dia de hj
    self.driver.set_window_size(1024, 768)
    self.driver.find_element(By.ID, "content_txtPalavrasChave").click()
    self.driver.find_element(By.ID, "content_txtPalavrasChave").send_keys("\"Raul Cruz Nadim\"")
    self.driver.find_element(By.ID, "content_btnBuscar").click()
    self.driver.find_element_by_class_name("joyride-close-tip").click()
    self.driver.find_element(By.ID, "content_lnkOrderByData").click()
    
    data_publi_elem = self.driver.find_element(By.ID, "content_dtgResultado_lblData_0")
    data_publi = data_publi_elem.get_attribute('innerHTML')
    print(data_publi)
    #self.driver.close()

# Acionamento
Base_se = TestDOESPSELENIUM()
Base_se.setup_method(1)
Base_se.test_dOESPSELENIUM()
#incluir teste aqui = verificar se a data do primeiro item é igual a data de hoje
  #se sim: mostrar o mais recente como NOVIDADE
  #se não: mostrar a mensagem 'sem novidade'
Base_se.teardown_method(1)



#texto
#data_publi_elem = driver.find_element(By.ID, "content_dtgResultado_lblData_0")
