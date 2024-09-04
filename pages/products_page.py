import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class ProductsPage(Base):  # Страница "Товары"

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    #  Locators

    products_word = '//h1[@class="all-products__title title-center"]'
    office_chairs = '(//a[contains(text(), "Офисные диваны, кресла, стулья")])[2]'
    office_chairs_2 = '//h3[contains(text(), "Офисные кресла и стулья")]'
    # Getters

    def get_products_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.products_word)))

    def get_office_chairs(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.office_chairs)))

    def get_office_chairs_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.office_chairs_2)))

    # Actions

    def click_office_chairs(self):
        self.get_office_chairs().click()
        self.driver.execute_script("window.scrollTo(0, 100);")
        print('Переход в "Офисные диваны, кресла, стулья" - ОК')

    def click_office_chairs_2(self):
        self.get_office_chairs_2().click()
        print('Переход в "Офисные кресла и стулья" - ОК')

    # Methods

    def assert_products_word(self):  # Метод: Проверка загрузки страницы "Товары"
        with allure.step("Assert products word"):
            Logger.add_start_step(method="assert_products_word")
            self.get_current_url()
            self.get_assert_word(self.get_products_word(), "КАТАЛОГ МЕБЕЛИ В МОСКВЕ")
            Logger.add_end_step(url=self.driver.current_url, method="assert_products_word")

    def office_chairs_select(self):  # Метод: Переход на страницу "Офисные кресла"
        with allure.step("Office chairs select"):
            Logger.add_start_step(method="office_chairs_select")
            self.click_office_chairs()
            self.click_office_chairs_2()
            Logger.add_end_step(url=self.driver.current_url, method="office_chairs_select")
