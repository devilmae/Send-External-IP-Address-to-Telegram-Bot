# 📡 Send External IP Address to Telegram Bot 🌐

A Python script that retrieves the external IP address of the machine running it and sends this information to a specified Telegram chat using a Telegram bot. This script utilizes the `pyTelegramBotAPI` library to interact with the Telegram API and the `requests` library to fetch the external IP address from `api.ipify.org`.

## Features

- 🌍 **Retrieve External IP**: Uses `api.ipify.org` to get the public IP address of the device.
- 📩 **Send Message to Telegram**: Sends the retrieved IP address to a specified Telegram chat using the Telegram bot API.

## Requirements

- Python 3.x
- `pyTelegramBotAPI` (Install via `pip install pyTelegramBotAPI`)
- `requests` (Install via `pip install requests`)

## Setup

1. **Create a Telegram Bot**:
   - Obtain a bot token from [BotFather](https://t.me/botfather) on Telegram.
   - Replace `'YOUR_TELEGRAM_BOT_API_TOKEN'` in the script with your bot token.

2. **Get Your Chat ID**:
   - Send a message to your bot on Telegram.
   - Find your chat ID using a bot like [userinfobot](https://t.me/userinfobot) or [@getidsbot](https://t.me/getidsbot).
   - Replace `'YOUR_CHAT_ID'` in the script with your chat ID.

3. **Update the Script**:
   - Clone or download this repository.
   - Replace the placeholders in the script with your actual API token and chat ID.

## Usage

1. **Save the Script**:
   Save the provided Python script to a file, e.g., `send_ip.py`.

2. **Run the Script**:
   Execute the script using Python:

   ```bash
   python send_ip.py
