import asyncio
from create_bot import bot, dp
from db_handler.db_class import drop_db, create_db, session_maker
from handlers.start import start_router
from middlewares.db import DataBaseSession
# from work_time.time_func import send_time_msg


async def on_startup(bot):

    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('Bot has finished work')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
