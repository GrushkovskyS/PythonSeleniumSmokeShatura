from selenium import webdriver

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.office_chairs_page import OfficeChairsPage
from pages.order_page import OrderPage
from pages.products_page import ProductsPage


def test_buy_product(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    # options.add_experimental_option("detach", True)
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)

    print("Start TEST")

    main_page = MainPage(driver)
    main_page.authorization()  # Авторизация
    main_page.select_products_point()  # Переход на страницу "Товары"

    products_page = ProductsPage(driver)
    products_page.assert_products_word()  # Проверка загрузки страницы "Товары"
    products_page.office_chairs_select()  # Переход на страницу "Офисные кресла"

    office_chairs_page = OfficeChairsPage(driver)
    office_chairs_page.assert_office_chairs_word()  # Проверка загрузки страницы "Офисные кресла"
    office_chairs_page.chairs_select()  # Выбор кресла

    cart_page = CartPage(driver)
    cart_page.assert_cart_page_word()  # Проверка загрузки страницы "Корзина"
    cart_page.cart_order_confirmation()  # Подтверждение заказа

    order_page = OrderPage(driver)
    order_page.assert_order_page_word()  # Проверка загрузки страницы "Оформление заказа"
    order_page.place_an_order()  # Оформление заказа

