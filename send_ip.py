import telebot
import requests

# Replace with your Telegram bot API token from BotFather
API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
# Replace with your chat ID
CHAT_ID = 'YOUR_CHAT_ID'

# Set up the bot
bot = telebot.TeleBot(API_TOKEN)

def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except requests.RequestException as e:
        return f"Error retrieving external IP address: {e}"

def send_ip_address():
    ip_address = get_external_ip()
    message = (
        "📡 **External IP Address Report** 🌐\n\n"
        f"Your external IP address is: `{ip_address}`\n\n"
        "🔍 This information was retrieved automatically. 🌟"
    )
    bot.send_message(CHAT_ID, message, parse_mode='Markdown')

if __name__ == '__main__':
    send_ip_address()
