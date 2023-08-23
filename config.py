# Copyright (C) 2023 DX-MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you use our codes try to donate here https://www.buymeacoffee.com/ziyankp

import re, os, time
from os import environ
from dotenv import load_dotenv
load_dotenv("config.env")
id_pattern = re.compile(r'^.\d+$') 
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # pyrogram client config
    API_ID    = environ.get("API_ID", "")
    API_HASH  = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
   
    # database config get this from mongodb
    DB_NAME = environ.get("DB_NAME","Dxbotz")     
    DB_URL  = environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    #start pic url this image will shown in start command get this from @DX_telegraphbot
    START_PIC   = environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '').split()]
    #the channel which need to force subscribed, channel username without @
    FORCE_SUB   = environ.get("FORCE_SUB", "") 
    #the log channel id must start in -100 this channel will be were the bot send logs
    LOG_CHANNEL = int(environ.get("LOG_CHANNEL", None))
    #prefix for the bot eg "!./#"
    PREFIX  = environ.get("PREFIX", ".")
    GENIUS_API = environ.get("GENIUS_API", "")
    CURRENCY_API = environ.get("CURRENCY_API", "")
    LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
    IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
    # wes response configuration
    #if your bot is web required give True or else False
    WEBHOOK = bool(environ.get("WEBHOOK", True))
    PORT = int(environ.get("PORT", "8080"))
    #the interval time to ping server
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "120"))
    #if your bot is running with web cmd pls copy the web link to ping server not down in 1 minutes
    PING_WEB = environ.get("PING_WEB", "") 
