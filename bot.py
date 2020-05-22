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

#await Bot.change_presence(status= discord.Status.idle)
#await Bot.change_presence(activity= discord.Game(name= 'By Blockman_'))


@Bot.command()
async def say(ctx, msg):
  await ctx.message.delete()
	await ctx.send(msg)
	print(f'[INFO]Bot sended a message: {msg}')


@Bot.command()
async def settings(ctx, type, type2, display):		
	if type == 'setdisplay':
		if type2 == 'activity':
			await Bot.change_presence(activity= discord.Game(name= display))
			usedcmd(f'{ctx.message.author}','settings setdisplay activity')
			print(f'[INFO]Bot changed activity display text to: {display}')



@Bot.command()
async def serverinfo(ctx):
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"{ctx.guild.name}", color=0xff0000, timestamp=ctx.message.created_at)
    embed.description=(
        f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
        f":flag_white: Регион **{ctx.guild.region}\n\nГлава сервера **{ctx.guild.owner}**\n\n"
        f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
        f":green_circle: Онлайн: **{online}**\n\n"
        f":black_circle: Оффлайн: **{offline}**\n\n"
        f":yellow_circle: Отошли: **{idle}**\n\n"
        f":red_circle: Не трогать: **{dnd}**\n\n"
        f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
        f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
        f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
        f":keyboard: Текстовых каналов: **{alltext}**\n\n"
        f":briefcase: Всего ролей: **{allroles}**\n\n"
        f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {ctx.guild.id}")
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)



#Calculator===================
OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

@Bot.command()
async def calc(ctx, a, operator, b):
    await ctx.send(f"{a} {operator} {b} = " + str(OPERATIONS[operator](int(a), int(b))))


#@Bot.command()
#async def help(ctx, page):
#	if page == '1':
		
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
	
#Bot.run(open('token1.txt', 'r').read()) # Строка запуска бота
