import motor.motor_asyncio
from config import DB_URL


cli = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
