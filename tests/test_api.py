import time
from api import API
from unittest import TestCase


class TestApi(TestCase):
    def test_api_1(self):
        """
        Test an api that accepts 3 requests every 5 seconds. With one call per second.

        Tests on 10 requests.
        """
        api = API(3, 5)

        expected_response = [
            True,
            True,
            True,
            False,
            False,
            True,
            True,
            True,
            False,
            False,
        ]

        response = []
        i = 0
        while i < 10:
            response.append(api.run(i))
            i += 1
            time.sleep(1)

        assert response == expected_response

    def test_api_2(self):
        """
        Test an api that accepts 5 requests every 3 seconds. With two calls per second.

        Tests on 10 requests.
        """
        api = API(5, 3)

        expected_response = [
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
        ]

        response = []
        i = 0
        while i < 10:
            response.append(api.run(i))
            i += 1
            response.append(api.run(i))
            i += 1
            time.sleep(1)

        assert response == expected_response
