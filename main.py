from bitcoin import get_bitcoin_price, check_price


price = get_bitcoin_price()

print(f"Bitcoin price: ${price}")

lower_limit = float(input("Enter lower limit: "))
upper_limit = float(input("Enter upper limit: "))

status = check_price(price, lower_limit, upper_limit)

if status == "below":
    print("Bitcoin price is below the lower limit.")
elif status == "above":
    print("Bitcoin price is above the upper limit.")
else:
    print("Bitcoin price is within the limits.")