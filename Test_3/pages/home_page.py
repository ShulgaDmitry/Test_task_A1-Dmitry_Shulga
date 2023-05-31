from Test_3.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


e_shop = (By.CSS_SELECTOR, 'a[href="/ru/c/shop"]')
phone_button = (By.CSS_SELECTOR, 'a[href="/ru/shop/c/phones"]')


class HomePage(BasePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_page(self):
        self.chrome_driver.get(self.base_url)

    def click_shop_phones_button(self):
        ActionChains(self.chrome_driver).move_to_element(self.find_element(e_shop)).click(
            self.find_element(phone_button)).perform()
