import requests
import time

# global variables
api_key = "api_key_of_coinmarketcap"
bot_token = "1717950175:AAHUAdok5XIe-K4OZ2DjnYe2laiG_G-z5M8"
chat_id = "telegram chat id"
time_int = 5 * 60
threshold = 0.2751


def get_doge_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()

    doge_price = response_json['data'][6]
    return doge_price['quote']['USD']['price']


def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"

    requests.get(url)


def main():
    price_list = []

    while True:
        price = get_doge_price()
        price_list.append(price)

        if price < threshold:
            send_message(chat_id=chat_id, msg=f"current Doge price: {price} and price of current holding: {price * 154}")

        time.sleep(time_int)


if __name__ == '__main__':
    main()
