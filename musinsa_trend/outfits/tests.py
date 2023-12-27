from django.test import TestCase
# from django.urls import resolve
# from django.http import HttpRequest
# from django.template.loader import render_to_string
from django.db import connections

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 단위 테스트=클래스, 기능 테스트 = 메서드 임?? 는 아닌 것 같은데 흠..
class OutfitViewsTest(TestCase):
    databases = ['default']  # 'other'

    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_raw_query(self):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT COUNT(*) FROM goods')
            result = cursor.fetchone()
        self.assertEqual(result[0], 2)

    def test_form_input(self):
        pass