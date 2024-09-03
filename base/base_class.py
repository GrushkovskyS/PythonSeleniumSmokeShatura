import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):  # Метод возвращающий URl
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    def get_assert_word(self, word, result):  # Метод проверяет проверочное слово
        value_text = word.text
        assert value_text == result
        print(f'Текст проверочного слова "{value_text}" совпадает - ОК')

    def assert_url(self, result):  # Метод проверяет URL
        get_url = self.driver.current_url
        assert get_url == result
        print(f"URL {get_url} совпадает - ОК")

    def assert_product_name(self, name):  # Метод проверяет имя товара
        value_product = name.text
        print(f"{value_product} - Название товара - ОК")

    def  assert_product_price(self, price):  # Метод проверяет цену товара
        value_product_price = price.text
        print(f"{value_product_price} - Цена товара - ОК")

    def assert_cart_product_name(self, name, name_cart):  # Метод сверяет имя товара с именем в корзине
        value_product = name.text
        value_product_cart = name_cart.text
        assert value_product_cart == value_product
        print(f"{value_product} = {value_product_cart} - Название товара совпадает с названием товара в корзине- ОК")

    def assert_cart_product_price(self, price, price_cart):  # Метод сверяет имя товара с именем в корзине
        value_product_price = price.text
        value_product_cart_price = price_cart.text
        assert value_product_cart_price == value_product_price
        print(f"{value_product_price} = {value_product_cart_price} - Цена товара совпадает с ценой товара в корзине- ОК")

    def get_screenshot(self):
        naw_date = datetime.datetime.utcnow().strftime(
            "%Y.%m.%d.%H.%M.%S")  # Переменная в которую записывается текущее время.
        name_screen = f'products{naw_date}.png'  # Создаём переменную в которую записываем скриншот, добавляем текущее время
        # и расширение.
        self.driver.save_screenshot(
            f'C:\\Users\\SAM\\PycharmProjects\\projectMI\\screenshot\\{name_screen}')  # делаем скриншот
        # в директорию "screen".
