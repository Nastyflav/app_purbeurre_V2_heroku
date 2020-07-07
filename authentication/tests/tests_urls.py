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
        self.change_pwd_url = reverse('password_change')
        self.change_pwd_done_url = reverse('password_change_done')
        self.reset_pwd_url = reverse('password_reset')
        self.reset_pwd_done_url = reverse('password_reset_done')

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

    def test_change_pwd_page_url(self):
        """To check the password modification url when requested"""
        self.assertEqual(self.change_pwd_url,
                         '/authentication/password_change/')

    def test_change_pwd_page_url_when_its_done(self):
        """To check the password change confirmation url when requested"""
        self.assertEqual(self.change_pwd_done_url,
                         '/authentication/password_change/done/')

    def test_reset_pwd_page_url(self):
        """To check the password reset url when requested"""
        self.assertEqual(self.reset_pwd_url, '/authentication/password_reset/')

    def test_reset_pwd_page_url_when_its_done(self):
        """To check the sent email confirmation url when requested"""
        self.assertEqual(self.reset_pwd_done_url,
                         '/authentication/password_reset/done/')
