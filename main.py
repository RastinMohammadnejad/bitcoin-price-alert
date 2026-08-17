import time

from bitcoin import get_bitcoin_price, check_price
from notifier import send_message


def main():
    lower_limit = float(input("Enter lower limit: "))
    upper_limit = float(input("Enter upper limit: "))
    check_interval = int(input("Check interval (seconds): "))

    if lower_limit >= upper_limit:
        print("Lower limit must be less than upper limit.")
        return

    if check_interval <= 0:
        print("Check interval must be greater than zero.")
        return

    previous_status = "normal"

    while True:
        price = get_bitcoin_price()

        if price is None:
            print("Failed to fetch Bitcoin price. Retrying...")
            time.sleep(check_interval)
            continue

        status = check_price(price, lower_limit, upper_limit)

        print(f"\nBitcoin price: ${price}")

        if status != previous_status:
            if status == "below":
                message = (
                    "Bitcoin Price Alert!!!\n\n"
                    f"Current price: ${price}\n"
                    f"Lower limit: ${lower_limit}\n\n"
                    "Bitcoin price is below your limit."
                )
                send_message(message)

            elif status == "above":
                message = (
                    "Bitcoin Price Alert!!!\n\n"
                    f"Current price: ${price}\n"
                    f"Upper limit: ${upper_limit}\n\n"
                    "Bitcoin price is above your limit."
                )
                send_message(message)

            else:
                message = (
                    "Bitcoin Price Alert!!!\n\n"
                    f"Current price: ${price}\n\n"
                    "Bitcoin price is back within the limits."
                )
                send_message(message)

            previous_status = status

        time.sleep(check_interval)


if __name__ == "__main__":
    main()