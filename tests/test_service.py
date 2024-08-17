from unittest import mock
from src.service import get_number

def test_using_return_value():
        with mock.patch('src.service.random.randint', return_value = 251), mock.patch('src.service.random.random', return_value = 502):
            assert get_number() == { "result1":251, "result2":500}

