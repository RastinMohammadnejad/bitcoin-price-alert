import time
from bitcoin import get_bitcoin_price, check_price


def main():
    lower_limit = float(input("Enter lower limit: "))
    upper_limit = float(input("Enter upper limit: "))

    previous_status = "normal"

    while True:
        price = get_bitcoin_price()
        status = check_price(price, lower_limit, upper_limit)

        print(f"\nBitcoin price: ${price}")

        if status != previous_status:
            if status == "below":
                print("Bitcoin price is below the lower limit.")
            elif status == "above":
                print("Bitcoin price is above the upper limit.")
            else:
                print("Bitcoin price is within the limits.")

            previous_status = status

        time.sleep(10)


if __name__ == "__main__":
    main()