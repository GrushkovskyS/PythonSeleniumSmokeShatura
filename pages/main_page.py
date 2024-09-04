import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):  # Главная страница
    url = 'https://www.shatura.com/'

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    #  Locators

    profile_button = '(//button[@class="header-middle__btn js_header_btn_menu_icon"])[1]'
    profile_button_2 = '(//button[@class="header-middle__btn js_header_btn_menu_icon"])[2]'
    button_login_1 = '//span[@class="menu-icon__link js-popup-view"]'
    button_log_pass = '//button[@class="btn btn__phone js-popup-view"]'
    user_mail = '(//input[@placeholder="E-mail"])[2]'
    user_password = '//input[@name="password"]'
    button_login = '//button[@data-action="user/login"]'
    profile_word = '(//a[@class ="menu-icon__link"])[2]'
    button_products = '(//li[@class="header-bottom-nav__item"])[1]'

    # Getters

    def get_profile_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.profile_button)))

    def get_button_login_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_login_1)))

    def get_button_log_pass(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_log_pass)))

    def get_user_mail(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_mail)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_profile_button_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.profile_button_2)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.profile_word)))

    def get_button_products(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_products)))

    # Actions

    def click_profile_button(self):
        self.get_profile_button().click()
        print('Кнопка "Профиль"  - ОК')

    def click_button_login_1(self):
        self.get_button_login_1().click()
        print('Кнопка "Вход"  - ОК')

    def click_button_log_pass(self):
        self.get_button_log_pass().click()
        print('Кнопка "Вход"  - ОК')

    def input_user_mail(self, user_mail):
        self.get_user_mail().send_keys(user_mail)
        print("User mail - ОК")

    def input_user_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("User password - ОК")

    def click_button_login(self):
        self.get_button_login().click()
        print('Кнопка "LOGIN" - ОК')

    def click_profile_button_2(self):
        self.get_profile_button_2().click()
        print('Кнопка "Профиль" - ОК')

    def click_button_products(self):
        self.get_button_products().click()
        print('Переход на страницу "Товары" - ОК')

    # Methods

    def authorization(self):  # Авторизация с проверкой
        with allure.step("authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_profile_button()
            self.click_button_login_1()
            self.click_button_log_pass()
            self.input_user_mail("ivan144550@gmail.com")
            self.input_user_password("212121")
            self.click_button_login()
            self.click_profile_button_2()
            self.get_assert_word(self.get_main_word(), "Мой профиль")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

    def select_products_point(self):  # Переход на страницу "Товары"
        with allure.step("Select products point"):
            Logger.add_start_step(method="select_products_point")
            self.click_button_products()
            Logger.add_end_step(url=self.driver.current_url, method="select_products_point")
