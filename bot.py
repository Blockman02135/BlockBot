import discord
from discord.ext import commands
import asyncio
import os


#Start-up message
@Bot.event #event
async def on_ready():
  #print(f'[STARTUP]Bot Online!\n[INFO]Bot Name: {Bot.user}\n[INFO]Bot ID: {Bot.user.id}') #start up message
  while True:
    await Bot.change_presence(activity= discord.Game(name= '&help'))
    await asyncio.sleep(20)
    await Bot.change_presence(activity= discord.Game(name= '&cmds'))
    await asyncio.sleep(20)

#Bot.load_extension("jishaku")

#<префикс>jsk py <тут дальше код который бдует выполняться>
#Но вы в нём должны использовать кое-какие другие названия переменных :
#_bot -> commands.Bot
#_ctx -> commands.Context

#Более коротко :
#_message -> _ctx.message
#_msg -> _ctx.message
#_guild -> _ctx.guild
#_channel -> _ctx.channel
#_author -> _ctx.message.author

#Command example========================================
#@Bot.command()
#async def command(ctx, other_atributes):
  #this code will work if command be used
#=======================================================

#@Bot.command()
#async def help(ctx, page):









token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
