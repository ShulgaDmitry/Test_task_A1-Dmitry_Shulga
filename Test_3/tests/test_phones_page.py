from Test_3.pages.phones_page import PhonesPage


def test_phones_page(chrome_driver):
    phone_page = PhonesPage(chrome_driver)
    phone_page.open_phones_page()
    phone_page.choose_random_phone()
    phone_page.choose_payment_option()
