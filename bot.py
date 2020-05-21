import discord
from discord.ext import commands
import asyncio
import os

Bot = commands.Bot(command_prefix='&')
Bot.remove_command('help')

@Bot.event
async def on_ready():
	await Bot.change_presence(activity= discord.Game(name= 'By Blockman_'))
	print(f"Bot Online!\nName - {Bot.user}\nID - {Bot.user.id}")

#def================
def usedcmd(member, cmd):
	print(f'{member} used bot command: {cmd}')



#Commands==========
@Bot.command()
async def hello(ctx):
	await ctx.send('Hello World!')
	
@Bot.command()
async def sayme(ctx):
	await ctx.send(f'{ctx.message.author.mention} - this is your name!')
	
@Bot.command()
async def sayme2(ctx):
	await ctx.send(f'{ctx.message.author} - this is your name! But no @')


#await Bot.change_presence(status= discord.Status.idle)
#await Bot.change_presence(activity= discord.Game(name= 'By Blockman_'))


@Bot.command()
async def say(ctx, msg):
	await ctx.send(msg)
	print(f'[INFO]Bot sended a message: {msg}')


@Bot.command()
async def settings(ctx, type, type2, display):		
	if type == 'setdisplay':
		if type2 == 'activity':
			await Bot.change_presence(activity= discord.Game(name= display))
			usedcmd(f'{ctx.message.author}','settings setdisplay activity')
			print(f'[INFO]Bot changed activity display text to: {display}')

#@Bot.command()
#async def help(ctx, page):
#	if page == '1':
		
token = os.environ.get('BOT_TOKEN')
	
#Bot.run(open('token1.txt', 'r').read()) # Строка запуска бота