from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import staff, bot


class Store_2(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    contacts = State()
    submit = State()


async def fsm_start(message: types.Message):
    await Store_2.product_id.set()
    await message.answer(text="Введите артикул товара:")


async def load_id_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await Store_2.next()
    await message.answer(text='Введите размер одежды')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await Store_2.next()
    await message.answer(text='Введите количество')


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await Store_2.next()
    await message.answer(text='Введите контакты')


async def load_contacts(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['contacts'] = message.text

        await Store_2.next()
        await message.answer(text=f"верны ли данные")
        keyboard = ReplyKeyboardMarkup(row_width=2)
        keyboard.add(KeyboardButton('Да'), KeyboardButton('Нет'))
        await message.answer(text=f"Артикул - {data['product_id']}"
                                  f"Размер - {data['size']},"
                                  f"Количество - {data['quantity']},"
                                  f"Контакты - {data['contacts']}",
                                  reply_markup=keyboard)


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            for i in staff:
                await bot.send_message(chat_id=i,
                                       text=f"Артикул - {data['product_id']}"
                                            f"Размер - {data['size']},"
                                            f"Количество - {data['quantity']},"
                                            f"Контакты - {data['contacts']}")
            await state.finish()
    elif message.text == 'Нет':
        await message.answer('Отменено!')
        await state.finish()


def register_fsm_order_handlers(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['order_product'])
    dp.register_message_handler(load_id_product, state=Store_2.product_id)
    dp.register_message_handler(load_size, state=Store_2.size)
    dp.register_message_handler(load_quantity, state=Store_2.quantity)
    dp.register_message_handler(load_contacts, state=Store_2.contacts)
    dp.register_message_handler(submit, state=Store_2.submit)
