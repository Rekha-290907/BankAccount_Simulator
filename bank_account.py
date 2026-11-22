
def deposit(bal, amt):
    if amt <= 0:
        raise ValueError("amount must be positive")
    return bal + amt
 
 
def withdraw(bal, amt):
    if amt <= 0:
        raise ValueError("amount must be positive")
    if amt > bal:
        raise ValueError("insufficient balance")
    return bal - amt
 
 
def interest(bal, rate):
    if rate < 0:
        raise ValueError("rate cannot be negative")
    return bal * rate / 100
 
 
def main():
    bal = 5000
    print(f"Opening balance: Rs. {bal}")
    bal = deposit(bal, 2000)
    print(f"After deposit of Rs. 2000: Rs. {bal}")
    bal = withdraw(bal, 1500)
    print(f"After withdrawal of Rs. 1500: Rs. {bal}")
    earned = interest(bal, 4)
    print(f"Interest at 4%: Rs. {earned:.2f}")
    print(f"Final balance: Rs. {bal + earned:.2f}")
 
 
if __name__ == "__main__":
    main()
