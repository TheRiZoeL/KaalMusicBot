from os import environ
# import logging
from pyrogram import Client, idle

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session_name = environ["SESSION_NAME"]

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client(session_name, api_id, api_hash, plugins=plugins)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> Ƙɑɑℓ Mυѕíc Usɘʀɓot Stʌʀtɘɗ')
idle()
app.stop()
print('\n>>> Ƙɑɑℓ Mυѕíc Usɘʀɓot Stoppɘɗ')
