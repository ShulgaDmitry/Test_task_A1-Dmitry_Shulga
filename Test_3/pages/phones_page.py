from Test_3.pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import random


list_phone = (By.CSS_SELECTOR, 'div[class="product-listing-item-title"]')
random_phone = (By.CSS_SELECTOR, 'div[class="product-listing-item-btn"]')
close_cookies = (By.CSS_SELECTOR, 'button[class="button button--primary cookie-panel-button"]')
select_variant_payment = (By.CSS_SELECTOR, 'span[class="select2-selection select2-selection--single"]')
order_window = (By.CSS_SELECTOR, 'div[class="price-block"]')
log_in_window = (By.CSS_SELECTOR, 'section[class="col-12-section--white col-12-section-content"]')
name_mobile = (By.XPATH, '//span[@itemprop="name"]/h1')
mobile_color = (By.XPATH, '//a[@class="disabled product-color--current product-color"]')
payment_method = (By.XPATH, '//span[@id="select2-priceBlock_selector_CURRENT_CONTRACT-container"]')


class PhonesPage(HomePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_phones_page(self):
        self.open_page()
        self.click_shop_phones_button()

    def choose_random_phone(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_contains('https://www.a1.by/ru/shop/c/phones'))
        self.find_element(close_cookies).click()
        list_phones = self.find_elements(list_phone)
        random_index = random.randrange(len(list_phones))
        get_the_deal_button = self.find_elements(random_phone)
        get_the_deal_button[random_index].click()
        WebDriverWait(self.chrome_driver, 5).until(EC.visibility_of_element_located(order_window))

    def choose_payment_option(self):
        select_mobile = self.find_element(name_mobile)
        select_color = self.find_element(mobile_color)
        ActionChains(self.chrome_driver).click(self.find_element(select_variant_payment)).send_keys(Keys.ARROW_DOWN).\
            send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        select_method = self.find_element(payment_method)
        print(f'\n Выбран {select_mobile.text} {select_color.text}, вариант оплаты: {select_method.text}')
        ActionChains(self.chrome_driver).click(self.find_element(select_variant_payment)).send_keys(Keys.TAB)\
            .send_keys(Keys.ENTER).perform()
        WebDriverWait(self.chrome_driver, 3).until(EC.visibility_of_element_located(log_in_window))

