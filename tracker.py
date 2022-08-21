from inspect import Parameter
import requests
import time
import telebot


# global variables
bot_token = ""
api_key = ""
chat_id = ""



bot=telebot.TeleBot(bot_token)

def get_id(coin):
    Id_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
    parameters = {
        'symbol': coin
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(Id_url, params=parameters, headers=headers)
    response_json = response.json()
    return response_json['data'][0]['id']

def get_coin_price(coin):
    id = get_id(coin)
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    parameters = {
        'id' :  id,
        'convert' : 'INR'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, params=parameters, headers=headers,)
    response_json = response.json()
    return response_json['data'][str(id)]['quote']['INR']['price']


@bot.message_handler(commands=['btc','eth','bnb','xrp','ada','sol'])
def price_bot(message):
    val = message.text
    coin = val.replace("/","")
    prices = get_coin_price(coin)
    chat = f"price of {coin} in INR: {prices}"
    bot.send_message(message.chat.id,chat)

bot.polling()
