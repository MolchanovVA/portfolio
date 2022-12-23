from selenium import webdriver
import pytest
import time


@pytest.fixture(autouse=True)
def open_site():
    pytest.driver = webdriver.Chrome('chromedriver.exe')
    # Устанавливаем не явное ожидание
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    pytest.driver.get('https://hh.kz')
    # Разворачиваем браузер в полноэкранный режим
    pytest.driver.maximize_window()
    time.sleep(3)


    yield
