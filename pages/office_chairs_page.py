import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class OfficeChairsPage(Base):  # Страница "Офисные кресла"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  Locators

    office_chairs_word = '//h1[@class="catalog__title title-center"]'
    filters = '//button[@class="filter__more js_filter_more"]'
    shade = '(//span[@class="filter__current js_filter_current"])[14]'
    shade_light = '//span[text()="Темный"]'
    color = '(//span[@class="filter__current js_filter_current"])[7]'
    window_color = '(//ul[@class="filter__dropdown filter__dropdown-checkbox js_filter_dropdown"])[6]'
    color_black = '(//li[@class="filter__checkbox checkbox"])[20]'
    size = '(//span[@class="filter__current js_filter_current"])[1]'
    height_size = '(//div[@aria-orientation="horizontal"])[1]'
    length_size = '//input[@id="catalogFilter_95_MAX"]'
    chair_604 = '//div[@data-product-id="161388"]'
    chair_604_name = '//a[text()="Кресло для руководителя Easy Chair 604"]'
    price_chair_604 = '//div[text()="31 313 ₽"]'
    button_add_to_cart_604 = '//button[@class="card__btn btn card__btn-1 card__btn_list add-to-basket-button-161388 js-add-to-basket "]'
    button_order = '//a[@class="add2cart__btn btn"]'

    # Getters

    def get_office_chairs_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.office_chairs_word)))

    def get_filters(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.filters)))

    def get_shade(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.shade)))

    def get_shade_light(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.shade_light)))

    def get_color(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_window_color(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.window_color)))

    def get_color_black(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.color_black)))

    def get_size(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.size)))

    def get_height_size(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.height_size)))

    def get_length_size(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.length_size)))

    def get_chair_604(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.chair_604)))

    def get_chair_604_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.chair_604_name)))

    def get_price_chair_604(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_chair_604)))

    def get_button_add_to_cart_604(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart_604)))

    def get_button_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_order)))

    # Actions

    def click_filters(self):
        self.get_filters().click()
        print("Все фильтры открыты - ОК")

    def click_shade(self):
        self.get_shade().click()
        print("Выбор оттенка - ОК")

    def click_shade_light(self):
        self.get_shade_light().click()
        print("Выбран оттенок: Тёмный - ОК")

    def click_color(self):
        self.get_color().click()
        print("Выбор Цвета - ОК")

    def scroll_window_color(self):
        action = ActionChains(self.driver)  # Создание переменной по управлению драйвером
        action.move_to_element(self.get_window_color()).perform()
        self.driver.execute_script("arguments[0].scrollBy(0, 150);", self.get_window_color())  # Скролл до Чёрного
        print("Прокрутка - ОК")

    def click_color_black(self):
        self.get_color_black().click()  # Выбор Цвета: Чёрный
        print("Выбор Цвета - ОК")

    def click_size(self):
        self.get_size().click()
        print("Выбор размера - ОК")

    def move_height_size(self):
        action = ActionChains(self.driver)  # Создание переменной по управлению драйвером
        action.click_and_hold(self.get_height_size()).move_by_offset(50, 0).release().perform()  # Изменение положения ползунка "Высота от" до 422
        print("Скролл высоты - ОК")

    def send_length_size(self):
        self.get_length_size().send_keys(Keys.DELETE*4)  # Очистка поля "Длинна до"
        self.get_length_size().send_keys(int(1000))  # Ввод в поле "Длинна до" значения 1000
        print('Изменение поля "Длинна до" - ОК')

    def move_to_chair_604(self):
        self.driver.execute_script("window.scrollTo(0, 1000);")
        action = ActionChains(self.driver)  # Создание переменной по управлению драйвером
        action.move_to_element(self.get_chair_604()).perform()  # Переход к элементу на странице
        print("Выделение товара - ОК")

    def click_button_add_to_cart_604(self):
        self.get_button_add_to_cart_604().click()
        print('Кнопка "В корзину" - ОК')

    def click_button_order(self):
        self.get_button_order().click()
        print('Кнопка "Оформить заказ" - ОК')

    # Methods

    def assert_office_chairs_word(self):  # Метод: Проверка загрузки страницы "Офисные кресла"
        Logger.add_start_step(method="assert_office_chairs_word")
        self.get_current_url()
        self.get_assert_word(self.get_office_chairs_word(),
                             "ОФИСНЫЕ ДИВАНЫ, КРЕСЛА, СТУЛЬЯ, ПОДГРУППА ТОВАРА: ОФИСНЫЕ КРЕСЛА")
        Logger.add_end_step(url=self.driver.current_url, method="assert_office_chairs_word")

    def chairs_select(self):
        Logger.add_start_step(method="chairs_select")
        self.click_filters()
        self.click_shade()  # Выбор оттенка:
        self.click_shade_light()  # Светлый
        time.sleep(2)
        self.assert_url(
            "https://www.shatura.com/goods/groups/ofisnye_divany_kresla_stulya/tov_subgroup-is-ofisnye_kresla/color-is-temnyy/")  # Проверка применения параметра фильтра Оттенка: "Тёмный"
        self.click_color()
        self.scroll_window_color()
        self.click_color_black()
        time.sleep(2)
        self.assert_url(
            "https://www.shatura.com/goods/groups/ofisnye_divany_kresla_stulya/tov_subgroup-is-ofisnye_kresla/cloth_color-is-chernyy/color-is-temnyy/")  # Проверка применения параметра фильтра Цвета: "Чёрный"
        self.click_size()
        time.sleep(2)
        self.move_height_size()
        time.sleep(2)
        self.assert_url("https://www.shatura.com/goods/groups/ofisnye_divany_kresla_stulya/price-from-422/tov_subgroup-is-ofisnye_kresla/cloth_color-is-chernyy/color-is-temnyy/")  # Проверка применения параметра фильтра Высоты: от 422
        self.click_size()
        time.sleep(2)
        self.send_length_size()
        time.sleep(2)
        self.assert_url(
            "https://www.shatura.com/goods/groups/ofisnye_divany_kresla_stulya/price-from-422-to-1000/tov_subgroup-is-ofisnye_kresla/cloth_color-is-chernyy/color-is-temnyy/")  # Проверка применения параметра фильтра Длинны: до 1000
        self.move_to_chair_604()
        self.assert_product_name(self.get_chair_604_name())  # Проверка названия товара
        self.assert_product_price(self.get_price_chair_604())  # Проверка цены товара
        time.sleep(2)
        self.click_button_add_to_cart_604()
        time.sleep(2)
        self.click_button_order()
        Logger.add_end_step(url=self.driver.current_url, method="chairs_select")
