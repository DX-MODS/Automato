import motor.motor_asyncio
from config import Config


cli = motor.motor_asyncio.AsyncIOMotorClient(Config.DB_URL)
