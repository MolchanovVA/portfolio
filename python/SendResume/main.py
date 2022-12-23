from selenium.webdriver.common.by import By
import pytest
from settings import vacancy, login, password, letter
import time

def test_all_pets(open_site):
    pytest.driver.find_element(By.XPATH, '//a[@data-qa="login"]').click()
    time.sleep(3)
    pytest.driver.find_element(By.XPATH, '//button[@data-qa="expand-login-by-password"]').click()
    time.sleep(3)
    pytest.driver.find_element(By.XPATH, '//input[@data-qa="login-input-username"]').send_keys(login)
    time.sleep(2)
    pytest.driver.find_element(By.XPATH, '//input[@data-qa="login-input-password"]').send_keys(password)
    time.sleep(2)
    pytest.driver.find_element(By.XPATH, '//button[@data-qa="account-login-submit"]').click()
    time.sleep(3)
    pytest.driver.find_element(By.XPATH, '//input[@data-qa="search-input"]').send_keys(vacancy)
    time.sleep(2)
    pytest.driver.find_element(By.XPATH, '//button[@data-qa="search-button"]').click()
    time.sleep(3)
    pytest.driver.find_element(By.XPATH, '//div[@data-qa="search-period-menu"]').click()
    time.sleep(3)
    pytest.driver.find_element(By.XPATH, '//div[@data-qa="order-by-1"]').click()
    time.sleep(3)

    elements = pytest.driver.find_elements(By.XPATH, '//a[@data-qa="vacancy-serp__vacancy_response"]')

    for i in range(len(elements)):

        handle1 = pytest.driver.window_handles
        pytest.driver.find_elements(By.XPATH, '//a[@data-qa="vacancy-serp__vacancy_response"]')[i].click()
        time.sleep(3)
        handle2 = pytest.driver.window_handles
        if handle1 != handle2:
            pytest.driver.switch_to.window(pytest.driver.window_handles[1])
            pytest.driver.close()
            pytest.driver.switch_to.window(pytest.driver.window_handles[0])
        else:
            pytest.driver.find_element(By.XPATH, '//button[@data-qa="vacancy-response-letter-toggle"]').click()
            time.sleep(2)
            pytest.driver.find_element(By.XPATH, '//textarea[@data-qa="vacancy-response-popup-form-letter-input"]').send_keys(letter)
            time.sleep(2)
            pytest.driver.find_element(By.XPATH, '//button[@data-qa="vacancy-response-submit-popup"]').click()
            time.sleep(2)



    assert pytest.driver.find_element(By.XPATH, '//input[@value="Тестировщик"]')