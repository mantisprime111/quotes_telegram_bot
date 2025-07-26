import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
import os
from dotenv import load_dotenv

load_dotenv()
dp = Dispatcher()

async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(router)
    await dp.start_polling(bot)
    
async def startup(dispatcher: Dispatcher):
    print('startup...')

async def shutdown(dispatcher: Dispatcher):
    print('shutdown...')

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')


