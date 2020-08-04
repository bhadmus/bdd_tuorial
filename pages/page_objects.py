from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from file import ref


class GuestShopper:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def setup(self):
        self.driver.get(ref.url)
        self.driver.maximize_window()

    def search_and_click(self):
        self.driver.find_element_by_id(ref.search_box).send_keys(ref.search_item)
        self.driver.find_element_by_css_selector(ref.search_button).click()

    def select_item(self):
        self.driver.execute_script("window.scrollTo(0,500);")
        self.driver.find_element_by_css_selector(ref.item).click()

    def add_to_cart(self):
        self.driver.find_element_by_id(ref.buy_button).click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ref.add_button)))
        self.driver.find_element_by_css_selector(ref.add_button).click()

    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ref.checkout_button)))
        self.driver.find_element_by_css_selector(ref.checkout_button).click()

    def verify_page(self):
        title = self.driver.title
        try:
            assert "Amazon Sign-In" in title
            print('Assertion Passed')
        except AssertionError:
            "Text not Found"
            print('Assertion Failed')
        # self.driver.quit()
