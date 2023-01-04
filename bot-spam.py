import discord
from discord.ext.commands import Bot

koala = Bot("$", intents=discord.Intents.all())
x = int(input("enter channel id here: "))
msg = input("enter bot spam message: ")
tkn = input("enter bot token: ")
times = int(input("enter the amount of messages: "))

@koala.event
async def on_ready():
    while True:
        await koala.get_channel(x).send(msg)

koala.run(tkn)
