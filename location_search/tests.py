from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client  # Use Django's test client
from .models import Search
# Create your tests here.


class DropdownViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Add setup code here. For example, you might create some objects:
        Search.objects.create(name='Test1', value=1)
        # YourModel.objects.create(name='Test2', value=2)

    def test_dropdown_view(self):
        response = self.client.get(reverse('your_view_name'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions here. For example, you might check that the
        # response contains the expected options:
        # self.assertContains(response, 'Test1')
        # self.assertContains(response, 'Test2')