def recharge(amount):
    if 5 <= amount <= 10:
        return amount
    elif amount == 25:
        return amount + 3
    elif amount == 50:
        return amount + 8
    elif amount == 100:
        return amount + 20


amount = 100
print("Your balance is now ${}".format(recharge(amount)))