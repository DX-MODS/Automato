from asyncio import gather

import httpx
from aiohttp import ClientSession

# Aiohttp Async Client
session = ClientSession()

# HTTPx Async Client
fetch = httpx.AsyncClient(
    http2=True,
    verify=False,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42"},
    timeout=httpx.Timeout(10),
)
