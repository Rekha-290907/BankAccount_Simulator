import pytest
from bank_account import deposit, withdraw, interest, safe_withdraw
 
 
def test_deposit_adds():
    assert deposit(1000, 500) == 1500
 
 
def test_deposit_negative_raises():
    with pytest.raises(ValueError):
        deposit(1000, -100)
 
 
def test_withdraw_reduces():
    assert withdraw(1000, 400) == 600
 
 
def test_withdraw_insufficient_raises():
    with pytest.raises(ValueError):
        withdraw(300, 500)
 
 
def test_interest_five_percent():
    assert interest(1000, 5) == 50
 
 
def test_interest_negative_rate_raises():
    with pytest.raises(ValueError):
        interest(1000, -2)
 
 
def test_safe_withdraw_allowed():
    assert safe_withdraw(2000, 1000) == 1000
 
 
def test_safe_withdraw_below_minimum_raises():
    with pytest.raises(ValueError):
        safe_withdraw(800, 500)
