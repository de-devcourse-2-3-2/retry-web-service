from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import re

from views import *


# 단위 테스트=클래스, 기능 테스트 = 메서드 임?? 는 아닌 것 같은데 흠..
class OutfitViewsTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_form_input(self):  # 이런 '스타일'로 할 수 있다는 말임
        pass