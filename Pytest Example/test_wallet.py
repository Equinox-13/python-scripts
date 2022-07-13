import pytest
from wallet import Wallet, InsufficientBalance

# fixtures helps in avoiding duplication in code
@pytest.fixture
def empty_wallet():
    '''Returns a wallet instance with zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a wallet instance with 20 balance'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_add_cash(empty_wallet):
    empty_wallet.add_cash(30)
    assert empty_wallet.balance == 30

def test_spend_cash_raises_insufficient_balance(empty_wallet):
    with pytest.raises(InsufficientBalance):
        empty_wallet.spend_cash(100)

# Parameterized test functions enables us to test different scenarios in
# a single function
@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20,2, 18),
])
def test_transactions(earned, spent, expected, empty_wallet):
    """
    Test different combination of values for the transaction
    :param earned: earned amount
    :param spent: spent amount
    :param expected: balance amount after the transactions
    :param empty_wallet: wallet with 0 balance
    """
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected
