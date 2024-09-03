import time

from base.base_class import Base

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  Locators

    order_page_word = '//h1[@class="ordering__title title"]'
    last_name = '//input[@name="last_name"]'
    name = '//input[@name="name"]'
    phone = '//input[@name="phone"]'
    city = '//input[@name="partner_city"]'
    street = '//input[@name="partner_street"]'
    house = '//input[@name="partner_house"]'
    flat = '//input[@name="partner_flat"]'
    entrance = '//input[@name="partner_entrance"]'
    floor = '//input[@name="partner_floor"]'
    marker_1 = '//div[@class="legend"]'
    radio_4 = '(//label[@class="ordering__radio"])[4]'
    radio_7 = '(//label[@class="ordering__radio"])[7]'
    delete_product = '//button[@class="ordering__block-top-del js-delete-partner-items"]'
    # Getters

    def get_order_page_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order_page_word)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_street(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_house(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.house)))

    def get_flat(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.flat)))

    def get_entrance(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.entrance)))

    def get_floor(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.floor)))

    def get_marker_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.marker_1)))

    def get_radio_4(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_4)))

    def get_radio_7(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_7)))

    def get_delete_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delete_product)))

    # Actions

    def send_last_name(self):
        self.get_last_name().send_keys("Ivanov")
        print('Ввод фамилии" - ОК')

    def send_name(self):
        self.get_name().send_keys("Ivan")
        print('Ввод имени" - ОК')

    def send_phone(self):
        self.get_phone().send_keys("999) 777-33-22")
        print('Ввод телефона" - ОК')

    def move_to_floor(self):
        action = ActionChains(self.driver)  # Создание переменной по управлению драйвером
        action.move_to_element(self.get_floor()).perform()  # Скролл к элименту
        print("Прокрутка - ОК")

    def send_city(self):
        self.get_city().send_keys("Москва")
        print('Ввод Города" - ОК')

    def send_street(self):
        self.get_street().send_keys("Шаболовка")
        print('Ввод Улицы" - ОК')

    def send_house(self):
        self.get_house().send_keys("38")
        print('Ввод Дома" - ОК')

    def send_flat(self):
        self.get_flat().send_keys("1")
        print('Ввод Квартиры" - ОК')

    def send_entrance(self):
        self.get_entrance().send_keys("1")
        print('Ввод Подъезда" - ОК')

    def send_floor(self):
        self.get_floor().send_keys("1")
        print('Ввод Этажа" - ОК')

    def move_marker_1(self):
        action = ActionChains(self.driver)  # Создание переменной по управлению драйвером
        action.move_to_element(self.get_marker_1()).perform()  # Скролл к элименту
        print("Прокрутка - ОК")

    def click_radio_4(self):
        self.get_radio_4().click()
        print('Услуги сборщика "ДА" - ОК')

    def click_radio_7(self):
        self.get_radio_7().click()
        print('Вывоз старой мебели "ДА" - ОК')

    def click_delete_product(self):
        self.get_delete_product().click()
        print('Удаляем товар из корзины" - ОК')

    # Methods

    def assert_order_page_word(self):  # Метод: Проверка загрузки страницы "Оформление заказа"
        self.get_current_url()
        self.get_assert_word(self.get_order_page_word(), "Оформление заказа")

    def place_an_order(self):
        self.send_last_name()
        # self.send_name()
        self.send_phone()
        self.move_to_floor()
        self.send_city()
        self.send_street()
        self.send_house()
        self.send_flat()
        self.send_entrance()
        self.send_floor()
        self.move_marker_1()
        self.click_radio_4()
        time.sleep(2)
        self.click_radio_7()
        time.sleep(2)
        self.click_delete_product()  # Вместо оформления заказа удаляем товар
        self.get_screenshot()
