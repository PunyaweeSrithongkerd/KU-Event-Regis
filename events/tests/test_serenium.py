from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
import requests
import unittest
import time

class test_redirect(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def button_redirect_to_regis(self):
        self.browser.get("http://localhost:8000/")

        regis_url = "http://localhost:8000/registered"
        self.browser.find_element_by_name('button_to_regis').click()
        self.assertEquals(
            self.browser.current_url,
            regis_url
            )
    def button_redirect_to_login(self):
        self.browser.get("http://localhost:8000/")

        login_url = "http://localhost:8000/login"
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url,
            login_url
            )
        
    def button_back_to_home(self):
        self.browser.get("http://localhost:8000/registered")

        home_url = "http://localhost:8000/"
        self.browser.find_element_by_name('button_to_home').click()
        self.assertEquals(
            self.browser.current_url,
            home_url
            )
