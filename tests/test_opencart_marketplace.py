import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_marketplace(driver): #косвенно проверяем, что попали куда хотели
    driver.get(driver.protocol+'://'+'demo.'+ driver.base_url)
    assert "Your Store" in driver.title

def test_opencart_marketplace_products_elements(driver):  # ищем products на странице marketplace, проверяем что количество продуктов совпадает
    products_count = 4     #ожидаемое количество продутов в нужном нам разделе
    driver.get(driver.protocol + '://' + 'demo.' + driver.base_url)
    products = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#content div.row div[class='product-thumb transition']")))
    assert len(products) == products_count #сравниваем количество полученных товаров с ожидаемым

@pytest.mark.parametrize("product, product_price, tag", [('MacBook', '$602.00', ''), ('iPhone', '$123.20', ''), ('Apple Cinema 30"', '$110.00', "/span[@class='price-new']"), ('Canon EOS 5D', '$98.00', "/span[@class='price-new']")])
def test_opencart_marketplace_products_price(driver, product, product_price, tag): #проверяем цены у продуктов (для тех, у кого есть скидка - берём price-new)
    driver.get(driver.protocol + '://' + 'demo.' + driver.base_url)
    #сначала по xpath ищем продукт, потом по дереву поднимаемся вверх и опускаемся в цену, которая должна содержать нужное нам значение
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='"+product+"']/../../p[@class='price']"+tag+"[contains(text(), '"+product_price+"')]")))


def test_opencart_marketplace_cocacola_swiperslide(driver):   #ищем кока-колу внизу
    driver.get(driver.protocol + '://' + 'demo.' + driver.base_url)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#carousel0 div.swiper-wrapper div[data-swiper-slide-index='3'] img[alt = 'Coca Cola']")))


def  test_opencart_marketplace_navbar_cameras(driver):  #ищем Cameras в меню навигации сверху
    driver.get(driver.protocol + '://' + 'demo.' + driver.base_url)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//nav[@id='menu']/div[@class='collapse navbar-collapse navbar-ex1-collapse']/ul[@class='nav navbar-nav']/li/a[text()='Cameras']")))
