import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

# from db_handler.db_class import PostgresHandler

load_dotenv()

# pg_db = PostgresHandler(config('PG_LINK'))
# scheduler = AsyncIOScheduler(timezone='Europe/Minsk')
admins = [int(admin_id) for admin_id in os.environ['ADMINS'].split(',')]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=os.environ['TOKEN'], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
