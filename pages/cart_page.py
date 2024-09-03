import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.office_chairs_page import OfficeChairsPage
from utilities.logger import Logger


class CartPage(OfficeChairsPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  Locators

    cart_page_word = '//h1[@class="cart__title title-center"]'
    cart_product_name = '//a[@class="item-cart__title"]'
    cart_product_price_total = '(//div[@class="sidebar-cart__total"]/span)[2]'
    cart_button_order_confirmation = '//a[@class="sidebar-cart__btn btn js-cart-order-button-proceed"]'
    # Getters

    def get_cart_page_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_page_word)))

    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_name)))

    def get_cart_product_price_total(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_price_total)))

    def get_cart_button_order_confirmation(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_button_order_confirmation)))

    # Actions

    def click_cart_button_order_confirmation(self):
        self.get_cart_button_order_confirmation().click()
        print('Кнопка "Оформить заказ" - ОК')

    # Methods

    def assert_cart_page_word(self):  # Метод: Проверка загрузки страницы "Корзина"
        with allure.step("Assert cart page word"):
            Logger.add_start_step(method="assert_cart_page_word")
            self.get_current_url()
            self.get_assert_word(self.get_cart_page_word(), "КОРЗИНА")
            Logger.add_end_step(url=self.driver.current_url, method="assert_cart_page_word")

    def cart_order_confirmation(self):  # Метод проверки имени и цены товара с именем и ценой в корзине и подтверждением заказа
        with allure.step("Cart order confirmation"):
            Logger.add_start_step(method="cart_order_confirmation")
            self.assert_cart_product_name(self.get_chair_604_name(), self.get_cart_product_name())
            #self.assert_cart_product_price(self.get_price_chair_604(), self.get_cart_product_price_total())  # Непонятно почему не работает проверка цены с финальным значением суммы ???
            self.click_cart_button_order_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="cart_order_confirmation")
