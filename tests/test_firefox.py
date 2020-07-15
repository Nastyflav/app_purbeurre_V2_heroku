#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-15
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from authentication.models import User
from search.models import Category, Product

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


def temp_user_creation():
    user = User.objects.create(email='selenium@user.test')
    user.set_password('test2020')
    user.save()


def db_init():
    data = Category(name="Pate à tartiner")
    data.save()

    data = Product(
        name="Ovomaltine",
        category_id=Category.objects.get(name="Pate à tartiner"),
        store="Leclerc, BioCoop",
        nutriscore="a",
        barcode="0189654870000",
        url="https://ovomaltine.fr",
        image="https://ovomaltine.fr/photo.jpg",
        lipids_for_100g="4.59",
        saturated_fats_for_100g="0.02",
        sugars_for_100g="1.54",
        salt_for_100g="3.25",
    )
    data.save()

    data = Product(
        name="Nutella",
        category_id=Category.objects.get(name="Pate à tartiner"),
        store="Auchan",
        nutriscore="b",
        barcode="012232370000",
        url="https://nutella.fr",
        image="https://nutella.fr/photo.jpg",
        lipids_for_100g="1.64",
        saturated_fats_for_100g="0.33",
        sugars_for_100g="2.20",
        salt_for_100g="1.06",
    )
    data.save()


class TestFirefox(StaticLiveServerTestCase):
    """To test a user story using Firefox"""
    def setUp(self):
        self.selenium = webdriver.Firefox(firefox_options=firefox_options)
        self.selenium.get(self.live_server_url)
        self.selenium.implicitly_wait(30)
        self.selenium.maximize_window()
        temp_user_creation()
        db_init()

    def tearDown(self):
        self.selenium.close()

    def test_login(self):
        """Test when the user wants to log in"""
        self.selenium.get('%s%s' % (self.live_server_url, '/authentication/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('selenium@user.test')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test2020')
        submit = self.selenium.find_element_by_id("submit-button")
        submit.send_keys(Keys.RETURN)

    def test_search_product_details(self):
        """To test when the user wants to search a prod and its details"""
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        query_input = self.selenium.find_element_by_id("query-main")
        query_input.send_keys('nutella')
        search = self.selenium.find_element_by_id("search-btn")
        search.send_keys(Keys.RETURN)
        product = WebDriverWait(self.selenium, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='details-link']")))
        product.click()

    def test_save_product(self):
        """To test when the user wants to save a product"""
        self.test_login()
        query_input = self.selenium.find_element_by_id("query-main")
        query_input.send_keys('nutella')
        search = self.selenium.find_element_by_id("search-btn")
        search.send_keys(Keys.RETURN)
        product = WebDriverWait(self.selenium, 30).until(
            EC.element_to_be_clickable((By.ID, "product-title")))
        product.click()
        substitute = WebDriverWait(self.selenium, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='save-btn']")))
        substitute.click()

    def test_logout(self):
        self.test_login()
        logout = WebDriverWait(self.selenium, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='logout']")))
        logout.click()
