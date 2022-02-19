import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_first(driver):
    driver.get(driver.protocol+'://'+ driver.base_url)
    assert "Cart Solution" in driver.title


def test_opencart_main_hero_elements(driver):  # на главной странице смотрим есть ли нужные нам элементы в первом разделе после меню навигации
    driver.get(driver.protocol+'://'+ driver.base_url)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#hero")))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#hero .hidden-xs a[href='https://www.opencart.com/index.php?route=cms/download']")))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#hero .hidden-xs a[href='https://www.opencart.com/index.php?route=cms/demo']")))
   #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#hero p.visible-xs-block a[href='https://www.opencart.com/index.php?route=cms/demo']")))
   #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#hero p.visible-xs-block a[href='https://www.opencart.com/index.php?route=cms/demo']")))
# - вот эти почему-то не работают, хотя практически идентичны верхним. Я не понимаю, почему.(через инспект элементов их тоже не видно)
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#hero div img.img-responsive[src='application/view/image/home/hero-image.png']")))

def test_opencart_main_features_xpath(driver): #пробуем искать с помощью xpath
    driver.get(driver.protocol+'://'+ driver.base_url)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Open-source and Free']")))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='common-home']/div[@id='business']/div[@class='container']/div[@class='page-header']/h2[text()='From corporations to local businesses']")))

