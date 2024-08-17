from unittest import mock, TestCase
from src.service import get_number
class TestService(TestCase):

    def test_using_return_value(self):
        with mock.patch('src.service.random.randint', return_value = 250):
            assert get_number() == 250

