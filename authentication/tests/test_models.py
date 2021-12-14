from django.contrib.auth.hashers import check_password
from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):
    # def test_Testing_file(self):
    #     self.assertEqual(1,1-0)

    def test_create_user(self):
        user=User.objects.create_user('abdo','a@gmail.com','123456741')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email,'a@gmail.com')
        self.assertTrue(check_password(password='123456741',encoded=user.password))
        self.assertEqual(user.username,'abdo')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user=User.objects.create_superuser('abdo','a@gmail.com','123456741')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email,'a@gmail.com')
        self.assertTrue(check_password(password='123456741',encoded=user.password))
        self.assertEqual(user.username,'abdo')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_raises_error_when_no_username_to_user(self):
        self.assertRaises(ValueError,User.objects.create_user,username="",email="a@gmail.com",password="123456")
    
    def test_raises_error_with_message_when_no_email_to_user(self):
        with self.assertRaisesMessage(ValueError,'The given email must be set'):
            User.objects.create_user(username="abdo",email="",password="123456")
    
    def test_raises_error_when_no_username_to_superuser(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username="",email="a@gmail.com",password="123456")
    
    def test_raises_error_with_message_when_no_email_to_superuser(self):
        with self.assertRaisesMessage(ValueError,'The given email must be set'):
            User.objects.create_superuser(username="abdo",email="",password="123456")

    def test_raises_error_when_superuser_isnot_staff(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username="abdo",email="@gmail.com",password="123456",is_staff=False)
    
    def test_raises_error_with_message_when_superuser_isnot_superuser(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username="abdo",email="a@gmail.com",password="123456",is_superuser=False)
