from django.test import TestCase
from django.test import LiveServerTestCase
# from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.db import connections

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


class OutfitViewsTest(LiveServerTestCase):
# class OutfitViewsTest(TestCase):
    databases = ['other']  # 'default',

    def setUp(self):
        # self.browser = webdriver.Chrome('chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_raw_query(self):
        with connections['other'].cursor() as cursor:
            cursor.execute('SELECT COUNT(*) FROM goods')
            result = cursor.fetchone()
        self.assertFalse(result[0], 0)

    # def test_top_styles_response(self):
    #     request = HttpRequest()
    #     response = index(request)
    #     expected_html = render_to_string('/Users/wonkyungkim/Documents/pythondev/retry-web-service/musinsa_trend/outfits/templates/index.html')
    #     # self.assertEqual(response.content.decode(), expected_html)
    #     self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html))

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스(Edith)는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다.
        self.browser.get("localhost:8000") # self.live_server_url,
        # header_text = self.browser.find_element('h1').text
        # self.assertIn('무신사 추천 코디로 보는 패션 트렌드', header_text)

    # def test_form_input(self):