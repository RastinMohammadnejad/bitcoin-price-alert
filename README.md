# Bitcoin Price Alert

A Python application that monitors the Bitcoin price and sends Telegram alerts when the price goes below or above predefined limits.

## Features

- Monitor the current Bitcoin price
- Set a lower Bitcoin price limit
- Set an upper Bitcoin price limit
- Configure the price checking interval
- Send a Telegram alert when the price goes below the lower limit
- Send a Telegram alert when the price goes above the upper limit
- Send a notification when the price returns to the defined range
- Prevent repeated alerts while the price remains in the same range
- Validate user input
- Handle Bitcoin API errors
- Handle Telegram API errors
- Store sensitive Telegram credentials in environment variables

## Technologies

- Python
- Requests
- python-dotenv
- REST API
- JSON
- Telegram Bot API
- CoinGecko API
- Git & GitHub

## Project Structure

```text
bitcoin-price-alert/
├── main.py
├── bitcoin.py
├── notifier.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

The application asks the user to enter:

1. Lower Bitcoin price limit
2. Upper Bitcoin price limit
3. Price checking interval in seconds

The application then periodically checks the current Bitcoin price through the CoinGecko API.

If the price goes below the lower limit, a Telegram alert is sent.

If the price goes above the upper limit, a Telegram alert is sent.

When the price returns to the defined range, a notification is sent again.

The application also prevents repeated alerts while the price remains in the same range.

## Installation

Clone the repository:

```bash
git clone https://github.com/RastinMohammadnejad/bitcoin-price-alert.git
```

Open the project directory:

```bash
cd bitcoin-price-alert
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

Replace the values with your own Telegram Bot Token and Chat ID.

Never share your `.env` file or Telegram Bot Token publicly.

## Usage

Run the application:

```bash
python main.py
```

The application will ask for the price limits and checking interval:

```text
Enter lower limit: 50000
Enter upper limit: 70000
Check interval (seconds): 60
```

The application will then start monitoring the Bitcoin price.

Example output:

```text
Bitcoin price: $63591
```

Example Telegram alert:

```text
Bitcoin Price Alert!!!

Current price: $70500
Upper limit: $70000

Bitcoin price is above your limit.
```

## Error Handling

The application handles common errors such as:

- Invalid numeric input
- Lower limit greater than or equal to upper limit
- Invalid checking interval
- Bitcoin API connection errors
- Telegram API connection errors
- Missing Telegram configuration

## Future Improvements

- Add support for other cryptocurrencies
- Add support for EUR and GBP
- Store Bitcoin price history
- Add a graphical user interface
- Add more notification methods
- Deploy the application for continuous monitoring

## Author

Rastin Mohammadnejad
