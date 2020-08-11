from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GuestShopper:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def setup(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close_banner(self, banner):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, banner)))
        self.driver.find_element_by_css_selector(banner).click()

    def search_and_click(self, search_box, search_word, search_button):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, search_box)))
        self.driver.find_element_by_css_selector(search_box).send_keys(search_word)
        self.driver.find_element_by_css_selector(search_button).click()

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0,6000);")

    def select_item(self, item):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, item)))
        self.driver.find_element_by_css_selector(item).click()

    def buy_option(self, buy):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.ID, buy)))
        self.driver.find_element_by_id(buy).click()

    def pick_location(self, locale):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locale)))
        self.driver.find_element_by_css_selector(locale).click()

    def add_to_cart(self, add):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, add)))
        self.driver.find_element_by_css_selector(add).click()

    def view_cart(self, view):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, view)))
        self.driver.find_element_by_css_selector(view).click()

    def proceed_to_checkout(self, checkout):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, checkout)))
        self.driver.find_element_by_css_selector(checkout).click()

    def verify_page(self, word):
        title = self.driver.title
        try:
            assert word in title
            print('Assertion Passed')
        except AssertionError:
            "Text not Found"
            print('Assertion Failed')
        # self.driver.quit()
