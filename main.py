import time
from bitcoin import get_bitcoin_price, check_price
from notifier import send_message


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
                message = f"Bitcoin price is below ${lower_limit}.\nCurrent price: ${price}"
                send_message(message)

            elif status == "above":
                message = f"Bitcoin price is above ${upper_limit}.\nCurrent price: ${price}"
                send_message(message)

            else:
                message = f"Bitcoin price is back within the limits.\nCurrent price: ${price}"
                send_message(message)

            previous_status = status

        time.sleep(10)


if __name__ == "__main__":
    main()