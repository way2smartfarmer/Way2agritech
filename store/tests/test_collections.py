from rest_framework import status
from rest_framework.test import APIClient


class TestCreateCollection:

    def test_if_user_is_anonymous_returns_401(self):
        # Arrange
        # Act
        client = APIClient()
        response = client.post('/store/products/', {'title': 'a'})

        # Asset(what behaviour expect)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self):
        # Arrange
        # Act
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title': 'a'})

        # Asset(what behaviour expect)
        assert response.status_code == status.HTTP_403_FORBIDDEN
