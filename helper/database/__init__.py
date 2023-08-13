import motor.motor_asyncio
from config import DBURL


cli = motor.motor_asyncio.AsyncIOMotorClient(DBURL)
