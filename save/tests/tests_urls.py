#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    """To test the save urls file"""
    def setUp(self):
        """Paths to the urls"""
        self.sub_url = reverse('save:substitution', args=[10])
        self.save_url = reverse('save:save')
        self.fav_url = reverse('save:favorites')
        self.del_url = reverse('save:delete', args=[1])

    def test_substitution_page_url(self):
        """To check the substitution url when requested"""
        self.assertEqual(self.sub_url, '/save/substitution/10')

    def test_saving_page_url(self):
        """To check the saving url when requested"""
        self.assertEqual(self.save_url, '/save/save/')

    def test_favorites_page_url(self):
        """To check the favorites url when requested"""
        self.assertEqual(self.fav_url, '/save/favorites/')

    def test_delete_page_url(self):
        """To check the favorites delete when requested"""
        self.assertEqual(self.del_url, '/save/delete/1')
