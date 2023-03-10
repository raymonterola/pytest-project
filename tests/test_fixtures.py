import pytest


class Company:
    def __init__(self, name: str, stock_symbol: str) -> None:
        self.name = name
        self.stock_symbol = stock_symbol
        
    def __str__(self) -> str:
        return f"{self.name}:{self.stock_symbol}"
    

@pytest.fixture
def company() -> Company:
    return Company(name='Fiverr', stock_symbol='FVRR')


def test_with_fixture(company: Company):
    print(f"Testing with fixture {company}")
    assert company.name == 'Fiverr'
    assert company.stock_symbol == 'FVRR'


@pytest.fixture(autouse=True)
def test_data(company: Company) -> dict:
    """This fixture modifies company and is automatically applied
    even if a test doesn't request it
    """
    company.name = 'Microsoft'
    company.stock_symbol = 'MSFT'
    return company


def test_with_fixture(company: Company):
    print(f"Testing with fixture {company}")
    assert company.name == 'Microsoft'
    assert company.stock_symbol == 'MSFT'
    
    
@pytest.mark.parametrize(
    'company_name',
    ['Tiktok', 'Instagram', 'Microsoft'],
    ids=['TIKTOK', 'INSTA', 'MSFT'],
)
def test_parametrized(company_name: str) -> None:
    """Runs test 3 times with multiple parameters"""
    print(f'Test with {company_name}')
    

def test_raises_exception() -> None:
    with pytest.raises(ZeroDivisionError) as e:
        10 / 0
    print(e)