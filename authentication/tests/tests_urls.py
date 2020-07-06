#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    """To test the authentication urls file"""
    def setUp(self):
        """Paths to the urls"""
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')
        self.signup_url = reverse('authentication:signup')
        self.profile_url = reverse('authentication:profile')
        self.modify_pwd_url = reverse('authentication:modify_pwd')

    def test_login_page_url(self):
        """To check the login url when requested"""
        self.assertEqual(self.login_url, '/authentication/')

    def test_logout_page_url(self):
        """To check the logout url when requested"""
        self.assertEqual(self.logout_url, '/authentication/deconnexion/')

    def test_signup_page_url(self):
        """To check the signup url when requested"""
        self.assertEqual(self.signup_url, '/authentication/inscription/')

    def test_profile_page_url(self):
        """To check the profile url when requested"""
        self.assertEqual(self.profile_url, '/authentication/profil/')

    def test_modify_pwd_page_url(self):
        """To check the password modification url when requested"""
        self.assertEqual(self.modify_pwd_url, '/authentication/modifier-mot-de-passe/')
