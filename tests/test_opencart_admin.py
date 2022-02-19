import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_admin_header(driver): #косвенно проверяем, что попали куда хотели
    driver.get(driver.protocol+'://'+'demo.'+ driver.base_url+'/admin/')
    assert "Administration" in driver.title

def test_admin_login(driver): #проверяем наличие нужных полей и входим
    driver.get(driver.protocol+'://'+'demo.'+ driver.base_url+'/admin/')
    input_username = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']"))) #находим инпут логина
    input_password = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))) #находим инпут пароля
    submit_login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit'][@class='btn btn-primary']")))#находим submit
    input_username.clear() #заранее чистим поля
    input_password.clear()
    input_username.send_keys('demo') #вводим значения
    input_password.send_keys('psswd')
    submit_login.submit() #нажимаем сабмит для входа
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='navigation']"))) #косвенно проверяем, что попали куда хотели
    


