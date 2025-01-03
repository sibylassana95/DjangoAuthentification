from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import PasswordReset

class AccountsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.user.save()

    def test_home_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        response = self.client.post(reverse('register'), {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_forgot_password_view(self):
        response = self.client.get(reverse('forgot-password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forgot_password.html')

        response = self.client.post(reverse('forgot-password'), {
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(PasswordReset.objects.filter(user=self.user).exists())

    def test_reset_password_view(self):
        password_reset = PasswordReset.objects.create(user=self.user)
        response = self.client.get(reverse('reset-password', kwargs={'reset_id': password_reset.reset_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reset_password.html')

        response = self.client.post(reverse('reset-password', kwargs={'reset_id': password_reset.reset_id}), {
            'password': 'newpassword',
            'confirm_password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword'))