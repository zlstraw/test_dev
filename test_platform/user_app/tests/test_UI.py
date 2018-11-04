from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from  django.contrib.auth.models import User
from project_app.models import Project


class LoginTests(StaticLiveServerTestCase):
    #fixtures = []

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)
        User.objects.create_user("admin","22@email.com","111")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(cls):
        # 初始化数据
        User.objects.create_user("admin","22@email.com","111")
        Project.objects.create(name = "测试平台项目",describe = "描述")

    def test_login_null(cls):
        cls.driver.get('%s%s' %(cls.live_server_url,'/'))
        username_input = cls.driver.find_element_by_name("username")
        username_input.send_keys("")
        password_input = cls.driver.find_element_by_name("password")
        password_input.send_keys("")
        sleep(2)
        cls.driver.find_element_by_id('LoginButton').click()
        error_hint = cls.driver.find_element_by_id("error").text
        print(error_hint)
        cls.assertEqual("用户名或者密码null",error_hint)
        sleep(5)

    def test_login_error(cls):
        cls.driver.get('%s%s' % (cls.live_server_url, '/'))
        username_input = cls.driver.find_element_by_name("username")
        username_input.send_keys("error")
        password_input = cls.driver.find_element_by_name("password")
        password_input.send_keys("error")
        sleep(2)
        cls.driver.find_element_by_id('LoginButton').click()
        error_hint = cls.driver.find_element_by_id("error").text
        print(error_hint)
        cls.assertEqual("用户名或密码错误", error_hint)
        sleep(5)

    def test_login_success(cls):
        cls.driver.get('%s%s' % (cls.live_server_url, '/'))
        username_input = cls.driver.find_element_by_name("username")
        username_input.send_keys("admin")
        password_input = cls.driver.find_element_by_name("password")
        password_input.send_keys("111")
        sleep(2)
        cls.driver.find_element_by_id('LoginButton').click()
        error_hint = cls.driver.find_element_by_class_name("navbar-brand").text
        print(error_hint)
        cls.assertEqual("测试平台", error_hint)
        sleep(5)
