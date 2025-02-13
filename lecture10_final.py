import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


class SearchTest(unittest.TestCase):
    """ Тестовый сценарий """

    def setUp(self):
        """Перед выполнением теста. Предварительная настройка браузера и переменных."""

        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("prefs", {'intl.accept_languages': 'en'})
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_search_selenide(self):
        """Тест #1 - Открытие страницы и проверка заголовка"""
        # Шаг 1. Открытие страницы
        self.driver.get('https://search.yahoo.com/')
        assert 'Yahoo Search - Web Search' in self.driver.title, 'Заголовок страницы не совпадает'

        # Шаг 2. Ожидание, пока элемент "поисковой строки" станет видимым
        elm = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.NAME, 'p')))
        elm.send_keys('selenide')
        elm.send_keys(Keys.ENTER)

        # Шаг 3. Проверяем, что первый результат – ссылка на сайт selenide.org.
        first_result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3.title a')))
        result_url = first_result.get_attribute('href')
        assert 'selenide.org' in result_url, 'Первый результат не является ссылкой на selenide.org'

        # Шаг 4. Перейти в раздел поиска изображений
        images_link = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Images')))
        images_link.click()

        # Шаг 5. Проверить, что первое изображение связано с сайтом selenide.org.
        first_image = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.img')))
        img_alt_text = first_image.get_attribute('alt')
        assert 'selenide' in img_alt_text.lower(), 'Первое изображение не связано с сайтом selenide.org'

        # Шаг 6. Вернуться в раздел поиска Все
        all_link = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'All')))
        all_link.click()

        # Шаг 7. Проверить, что первый результат такой же, как и на шаге 3.
        new_first_result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.reg:nth-child(1) a')))
        new_result_url = new_first_result.get_attribute('href')
        assert result_url == new_result_url, 'Первый результат не совпадает с предыдущим'

    def tearDown(self):

        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
