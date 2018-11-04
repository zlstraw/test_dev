from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from project_app.models import Project

# Create your tests here.
class projectTest(TestCase):

    def setUp(self):
        User.objects.create_user("tt","tt@email.com","11")
        Project.objects.create(name="test platform",describe="describe")
        self.client = Client()
        login_data = {"username":"tt","password":"11"}
        self.client.post('/login_action/',data = login_data)

    def test_project_add(self):
        Project.objects.create(name="test tt",describe="abc")
        project = Project.objects.get(name="test tt")
        print(project.describe)
        self.assertEqual(project.describe,"abc")

    def test_project_update(self):
        p = Project.objects.get(name="test platform")
        p.describe = "tt"
        p.save()
        #print(p.describe)
        p2 = Project.objects.get(name="test platform")
        self.assertEqual(p2.describe,"tt")

    def test_project_delete(self):
        project = Project.objects.get(name="test platform")
        project.delete()
        projects = Project.objects.all()
        self.assertEqual(len(projects), 0)

    def test_project_manage(self):
        response = self.client.post('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        #print(project_html)
        self.assertEqual(response.status_code,200)
        self.assertIn("退出",project_html)
        self.assertIn("test platform",project_html)
