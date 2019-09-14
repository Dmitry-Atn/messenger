from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Message
from django.urls import reverse
from .serializers import MessagesSerializer


# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_message(body, sender=None, recipient=None):
        Message.objects.create(sender=sender, recipient=recipient, body=body)

    def setUp(self):
        # test messages
        self.create_message("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        self.create_message("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        self.create_message("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        self.create_message("Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_messages(self):
        """

        """
        # hit the API endpoint
        response = self.client.get(
            reverse("messages-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Message.objects.all()
        serialized = MessagesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)