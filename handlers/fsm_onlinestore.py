from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from Database import db


class Store(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    submit = State()


async def fsm_start(message: types.Message):
    await Store.product_id.set()
    await message.answer(text="Введите артикул товара:")


async def load_id_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await Store.next()
    await message.answer(text='Введите размер одежды')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await Store.next()
    await message.answer(text='Введите количество')


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await Store.next()
    await message.answer(text=f"верны ли данные")
    keyboard = ReplyKeyboardMarkup(row_width=2)
    keyboard.add(KeyboardButton('Да'), KeyboardButton('Нет'))
    await message.answer(text=f"Артикул - {data['product_id']}"
                              f"Размер - {data['size']},"
                              f"Количество - {data['quantity']},",
                              reply_markup=keyboard)


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            await db.insert_product(product_id=data['product_id'],
                                    size=data['size'],
                                    quantity=data['quantity'])
            await message.answer('Отлично! Регистрация пройдена.')
            await state.finish()
    elif message.text == 'Нет':
        await message.answer('Отменено!')
        await state.finish()


def register_fsm_store_handlers(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['register_product'])
    dp.register_message_handler(load_id_product, state=Store.product_id)
    dp.register_message_handler(load_size, state=Store.size)
    dp.register_message_handler(load_quantity, state=Store.quantity)
    dp.register_message_handler(submit, state=Store.submit)
