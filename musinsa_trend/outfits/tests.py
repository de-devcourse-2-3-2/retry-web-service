from django.test import TestCase
# from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
# from django.db import connections

from selenium import webdriver
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import re
from .views import *
# from views import *


def remove_csrf(html_code):
    csrf_regex = r'&lt;input[^&gt;]+csrfmiddlewaretoken[^&gt;]+&gt;'
    return re.sub(csrf_regex, '', html_code)


class OutfitViewsTest(TestCase):
    databases = ['default']  # 'other'

    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # def test_raw_query(self):
    #     with connections['default'].cursor() as cursor:
    #         cursor.execute('SELECT COUNT(*) FROM goods')
    #         result = cursor.fetchone()
    #     self.assertEqual(result[0], 2)

    def test_top_styles_response(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('/Users/wonkyungkim/Documents/pythondev/retry-web-service/musinsa_trend/outfits/templates/index.html')
        # self.assertEqual(response.content.decode(), expected_html)
        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html))


    def test_form_input(self):
        pass