from unittest import mock
from src.service import get_number

@mock.patch('src.service.random.randint')
def test_get_number_call_done(mock_randint):
    get_number()
    mock_randint.assert_called_once()

def test_using_return_value():
        with mock.patch('src.service.random.randint', return_value = 251), mock.patch('src.service.random.random', return_value = 500):
            assert get_number() == { "result1":251, "result2":500}

