import time

from bitcoin import get_bitcoin_price, check_price
from notifier import send_message, create_alert_message


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def main():
    lower_limit = get_number("Enter lower limit: ")
    upper_limit = get_number("Enter upper limit: ")
    check_interval = get_number("Check interval (seconds): ")

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
            message = create_alert_message(
                status,
                price,
                lower_limit,
                upper_limit
            )

            send_message(message)

            previous_status = status

        time.sleep(check_interval)


if __name__ == "__main__":
    main()