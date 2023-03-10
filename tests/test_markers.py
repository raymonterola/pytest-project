import pytest

@pytest.mark.new
def test_marked_new() -> None:
    assert True
    
    
@pytest.mark.skip
def test_skipped_test():
    assert False
    

z = None
    
@pytest.mark.parametrize(
    'x',
    [None, 'ok'],
    ids=['NON','OK']
)
def test_parametrized_skip(x) -> None:
    print(x)
    if x is None:
        pytest.skip()  # manually skip test
    assert x is not None


@pytest.mark.skipif(z is None, reason='Test skipped because x is None')
def test_skipped_with_condition() -> None:
    assert False
    

@pytest.mark.xfail
def test_ignored_if_fails():
    assert False
    