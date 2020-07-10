#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-06
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase
from django.core import mail


class MailTest(TestCase):
    """Test the sent emails"""
    def test_sent_emails(self):
    "To check if the emails are well sent by the system"
        mail.send_mail('Mail subject', 'Message',
                       'test@dj.com',
                       ['support@purbeurre.fr']
                       )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Mail subject')
        self.assertEqual(mail.outbox[0].body, 'Message')
        self.assertEqual(mail.outbox[0].from_email, 'test@dj.com')
        self.assertEqual(mail.outbox[0].to, ['support@purbeurre.fr'])
