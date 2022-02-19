from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration_header(driver): #косвенно проверяем, что попали куда хотели
    driver.get(driver.protocol+'://'+ driver.base_url+'/index.php?route=account/register')
    assert "OpenCart - Account Register" in driver.title

def test_registration_elements(driver): #проверяем поля на странице регистрации пользователя
    driver.get(driver.protocol + '://' + driver.base_url + '/index.php?route=account/register')
    label_username = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[@for='input-username'][text()='Username']")))    #ищем пару лейблов
    label_firstname = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[@for='input-firstname'][text()='First Name']")))
    label_lastname = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[@for='input-lastname'][text()='Last Name']")))
    input_username = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    input_firstname = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    input_lastname = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))#ищем поля для ввода
