#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-15
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from selenium import webdriver
from django.test import TestCase


class TestChrome(TestCase):
    """To test the user story using Chrome browser"""
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='./chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('https://purbeurreflavien.herokuapp.com/')

        # Elle remarque que le mot Planning
        # figure dans le titre de la page
        self.assertIn('Beurre', self.browser.title)  #
        self.fail('Test terminé !')