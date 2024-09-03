import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print('--- Начало теста №1 ---')
    yield
    print("--- Конец теста №1 ---")
