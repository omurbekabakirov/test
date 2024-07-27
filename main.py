import logging
from aiogram.utils import executor
from Database import db
from config import dp
from handlers import commands, fsm_onlinestore, fsm_clients_order


async def on_startup(_):
    await db.create_table()

commands.register_commands(dp=dp)
fsm_onlinestore.register_fsm_store_handlers(dp=dp)
fsm_clients_order.register_fsm_order_handlers(dp=dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
