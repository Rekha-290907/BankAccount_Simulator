MIN_BALANCE = 500   # Minimum balance to be kept in the account


def deposit(bal, amt):
    if amt <= 0:
        raise ValueError("Amount must be positive")
    return bal + amt


def withdraw(bal, amt):
    if amt <= 0:
        raise ValueError("Amount must be positive")
    if amt > bal:
        raise ValueError("Insufficient balance")
    return bal - amt


def safe_withdraw(bal, amt):
    if amt <= 0:
        raise ValueError("Amount must be positive")
    if bal - amt < MIN_BALANCE:
        raise ValueError("Minimum balance of Rs. 500 must be kept")
    return withdraw(bal, amt)


def interest(bal, rate):
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    return bal * rate / 100


def main():
    bal = 5000

    print(f"Opening balance: Rs. {bal}")
    print(f"Minimum balance required: Rs. {MIN_BALANCE}")

    bal = deposit(bal, 2000)
    print(f"After deposit of Rs. 2000: Rs. {bal}")

    bal = safe_withdraw(bal, 1500)
    print(f"After withdrawal of Rs. 1500: Rs. {bal}")

    earned = interest(bal, 4)
    print(f"Interest at 4%: Rs. {earned:.2f}")

    print(f"Final balance: Rs. {bal + earned:.2f}")


if __name__ == "__main__":
    main()