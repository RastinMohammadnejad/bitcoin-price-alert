# Bitcoin Price Alert

A Python application that monitors the Bitcoin price and sends alerts when the price crosses predefined limits.

## Features

- Monitor Bitcoin price
- Set a lower price limit
- Set an upper price limit
- Send an alert when the price goes below the lower limit
- Send an alert when the price goes above the upper limit
- Prevent repeated alerts while the price remains in the same range

## Technologies

- Python
- Requests
- REST API
- JSON
- Git & GitHub

## Project Structure

```text
bitcoin-price-alert/
├── main.py
├── bitcoin.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

The application periodically checks the current Bitcoin price through an API.

If the price goes below the configured lower limit, the application sends a warning alert.

If the price goes above the configured upper limit, the application sends an alert indicating that the upper limit has been reached.

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

Activate the virtual environment:

```bash
source .venv/Scripts/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

## Author

Rastin Mohammadnejad