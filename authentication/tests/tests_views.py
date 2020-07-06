#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import User


class TestViews(TestCase):
    """To test the authentication app"""
    def setUp(self):
        """ Create a temp user to perform tests"""
        self.client = Client()
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')
        self.profile_url = reverse('authentication:profile')
        self.signup_url = reverse('authentication:signup')
        self.modify_pwd_url = reverse('authentication:modify_pwd')
        self.user = User.objects.create(email='user@test.dj')
        self.user.set_password('supertest2020')
        self.user.save()

    def test_signup_page_returns_200(self):
        """To test the status code and the login page"""
        response = self.client.get(self.signup_url)
        self.assertTemplateUsed(response, 'registration/account_creation.html')
        self.assertEqual(response.status_code, 200)

    def test_login_redirection_when_validation(self):
        """To test redirection when login action is completed"""
        response = self.client.post(self.login_url, {
            'username': 'user@test.dj',
            'password': 'supertest2020'
        })
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200)

    def test_signup_redirection_when_validation(self):
        """To check the redirection when the account creation is accepted"""
        response = self.client.post(self.signup_url, {
            'email': 'newuser@test.dj',
            'password1': 'supernouveau',
            'password2': 'supernouveau'
        })
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200)

    def test_profile_page_view(self):
        """To check the profile method in views file"""
        response = self.client.get(self.profile_url)
        self.assertTemplateUsed(response, 'registration/user_profile.html')
        self.assertEqual(response.status_code, 200)

    def test_login_page_returns_200(self):
        """To test the status code and the login page"""
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response.status_code, 200)

    def test_logout_redirection(self):
        """To test the redirection when the user logs out"""
        response = self.client.get(self.logout_url)
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200)

    def test_check_password(self):
        """To check the current user password"""
        self.client.login(username='user@test.dj', password='supertest2020')
        user = User.objects.get(email='user@test.dj')
        self.assertEqual(user.check_password('supertest2020'), True)

    def test_modify_password_with_success(self):
        """To test when an user success to change his password"""
        self.client.login(username='user@test.dj', password='supertest2020')
        response = self.client.post(self.modify_pwd_url, {
            "old_password": "supertest2020",
            "new_password1": "supertest2021",
            "new_password2": "supertest2021"
        })
        self.assertRedirects(
            response, '/authentication/modifier-mot-de-passe/done/',
            status_code=302, target_status_code=200)

        user = User.objects.get(email='user@test.dj')
        self.assertEqual(user.check_password('supertest2021'), True)

    def test_modify_password_failure(self):
        """To test when an user doesn't manage to change his password"""
        self.client.login(username='user@test.dj', password='supertest2020')
        response = self.client.post(self.modify_pwd_url, {
            "old_password": "supertest2020",
            "new_password1": "supertest2021",
            "new_password2": "supertest2022"
        })
        self.assertEqual(response.status_code, 200)