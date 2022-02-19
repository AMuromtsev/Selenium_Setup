
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product_header(driver): #косвенно проверяем, что попали куда хотели
    driver.get(driver.protocol+'://'+'demo.'+ driver.base_url+'/index.php?route=product/product&product_id=40')
    assert "iPhone" in driver.title

def test_product_content(driver): #проверяем информацию о продукте
    driver.get(driver.protocol + '://' + 'demo.' + driver.base_url + '/index.php?route=product/product&product_id=40')
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-4']/h1[text()='iPhone']")))
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-4']/ul[@class='list-unstyled']/li[text()='Brand: ']/a[text()='Apple']")))
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-4']/ul[@class='list-unstyled']/li[text()='Product Code: product 11']")))
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-4']/ul[@class='list-unstyled']/li[text()='Availability: Out Of Stock']")))

def test_product_check_price(driver): #проверяем цену
    price = '$123.20'
    driver.get(driver.protocol + '://' + 'demo.' + driver.base_url + '/index.php?route=product/product&product_id=40')
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='col-sm-4']/ul[@class='list-unstyled']/li/h2[text()='"+price+"']")))


def test_product_check_description(driver): #проверяем описание (для айфона)
    driver.get(driver.protocol + '://' + 'demo.' + driver.base_url + '/index.php?route=product/product&product_id=40')
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[@class='intro'][contains(text(),'iPhone is a revolutionary new mobile phone that allows you to make a call by simply tapping a name or number in your address book, a favorites list, or a call log. It also automatically syncs all your contacts from a PC, Mac, or Internet service. And it lets you select and listen to voicemail messages in whatever order you want just like email.')]")))


def test_product_add_to_cart(driver): #проверяем добавление в корзину
    driver.get(driver.protocol + '://' + 'demo.' + driver.base_url + '/index.php?route=product/product&product_id=40')
    add_to_cart = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    add_to_cart.click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
