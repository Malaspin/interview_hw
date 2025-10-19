import pytest
from main import balance

test_data = [
    (r'(((([{}]))))', 'Сбалансированно'),
    (r'[([])((([[[]]])))]{()}', 'Сбалансированно'),
    (r'{{[()]}}', 'Сбалансированно'),
    (r'}{}', 'Несбалансированно'),
    (r'{{[(])]}}', 'Несбалансированно'),
    (r'[[{())}]', 'Несбалансированно')
]

@pytest.mark.parametrize('data, expect', test_data)
def test_balance(data, expect):
    assert balance(data=data) == expect
