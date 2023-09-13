import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
import cmc
from keys import TGtoken
from cmc import *

bot = Bot(token=TGtoken)
dp = Dispatcher()


@dp.message(F.text == '/start')
async def start_mess(message: Message):
    await message.answer(
        'Этот бот создан для просмотра цен на криптовалюты\nЧто-бы начать введите /price')


@dp.message(F.text == '/price')
async def price_mess(message: Message):
    await message.answer('Выберите валюту, в которой хотите узнать цену:', reply_markup=currency_keyboard)


@dp.message(lambda message: message.text.upper() in ['USD', 'RUB', 'EUR'])
async def process_currency(message: types.Message):
    global input_currency
    input_currency = message.text.upper()
    await message.answer('Введите название криптовалюты либо выберите популярную на клавиатуре',
                         reply_markup=coin_keyboard)


@dp.message(lambda message: not message.text.startswith('/'))
async def process_crypto_currency(message: types.Message):
    global input_coin
    input_coin = message.text.upper()
    result = await check_coin(input_coin, input_currency)
    logo = await cmc.logo(input_coin)
    await message.answer_photo(photo=logo)
    await message.answer(f'Логотип {input_coin}\n{result}')
    await message.answer('Введите новое название:')



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
