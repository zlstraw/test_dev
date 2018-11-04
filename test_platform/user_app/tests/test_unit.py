from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from user_app.views import index

class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create_user("test01","test01@email.com","")

    def test_user_create(self):
        User.objects.create_user("test02","test02@email.com","test654321")
        user = User.objects.get(username="test02")
        print(user.email)
        print(user.password)
        self.assertEqual(user.email,"test02@email.com")

    def test_user_select(self):
        user = User.objects.get(username="test01")
        self.assertEqual(user.email,"test01@email.com")

    def test_user_update(self):
        user = User.objects.get(username="test01")
        user.username = "test02"
        user.email = "test02@email.com"
        user.save()
        user2 = User.objects.get(username="test02")
        self.assertEqual(user2.email,"test02@email.com")

    def test_user_delete(self):

        user = User.objects.get(username="test01")
        user.delete()
        users = User.objects.all()
        self.assertEqual(len(users),0)


# 单元测试
class indexTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):

        response = self.client.get('/')
        #print(response.content.decode("utf-8"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')


class loginTest(TestCase):

    def setUp(self):
        User.objects.create_user("test01","test01@email.com","111111")
        self.client = Client()

    def test_login_null(self):
        login_data = {"username":"", "password":""}
        response = self.client.post('/login_action/', data = login_data)
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code,200)
        self.assertIn("用户名或者密码为空",login_html)

    def test_login_error(self):
        login_data = {"username":"2333", "password":"23333"}
        response = self.client.post('/login_action/', data = login_data)
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code,200)
        self.assertIn("用户名或者密码错误",login_html)


    def test_login_success(self):
        login_data = {"username":"test01", "password":"111111"}
        response = self.client.post('/login_action/', data = login_data)
        self.assertEqual(response.status_code,302)



class logoutTest(TestCase):

    def setUp(self):
        User.objects.create_user("test01","aaa@email.com","111")
        self.client = Client()
        login_data = {"username":"test01", "password":"111"}
        response = self.client.post('/login_action/', data = login_data)

    def test_logout(self):
        response = self.client.post('/logout/')
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code,302)