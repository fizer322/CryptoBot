from keys import cmcAPI, url
import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

currency_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="USD"),
            KeyboardButton(text="RUB"),
            KeyboardButton(text="EUR"),
        ],
    ],
    resize_keyboard=True,
    selective=True,
)
coin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="BTC"),
            KeyboardButton(text="ETH"),
            KeyboardButton(text="BNB"),
            KeyboardButton(text="XRP"),
            KeyboardButton(text="DOGE"),
            KeyboardButton(text="ADA"),
        ],
    ],
    resize_keyboard=True,
    selective=True,
)


async def check_coin(input_coin, input_currency):
    params = {
        'symbol': input_coin,
        'convert': input_currency,
    }
    headers = {
        'X-CMC_PRO_API_KEY': cmcAPI,
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        coin_price = data['data'][input_coin]['quote'][input_currency]['price']
        market_cap = data["data"][input_coin]["quote"][input_currency]["market_cap"]
        return f'Цена: {round(coin_price, 4)} {input_currency}\nКапитализация: {int(market_cap)} {input_currency}'
    else:
        return 'Ошибка при запросе данных, попробуйте позже'


async def logo(input_coin):
    api_url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    params = {
        'symbol': input_coin,
    }
    headers = {
        'X-CMC_PRO_API_KEY': cmcAPI,
    }
    response = requests.get(api_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        coin_data = data['data'][input_coin]
        logo_url = coin_data['logo']

        return logo_url
    else:
        return 'Ошибка при получении данных о монете'
