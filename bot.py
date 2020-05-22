import discord
from discord.ext import commands
import asyncio
import os
import pyowm

owm = pyowm.OWM('9963f6627710292d5125e8200fc5b2b5', language= 'ru')


#Start-up message
@Bot.event #event
async def on_ready():
  print(f'[STARTUP]Bot Online!\n[INFO]Bot Name: {Bot.user}\n[INFO]Bot ID: {Bot.user.id}') #start up message

Bot.load_extension("jishaku")

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

@Bot.command()
async def help(ctx, page):





#weather-command=========================
@Bot.command()
async def weather(ctx, *, arg):
    observation = owm.weather_at_place(arg)
    w = observation.get_weather()
    prs = w.get_pressure()
    tmp = w.get_temperature('celsius')
    hmd = w.get_humidity()
    cld = w.get_clouds()
    wnd = w.get_wind()
    wnds = wnd.get('speed')
    wnds_str = ''
    rn = w.get_rain()
    emb = discord.Embed(
        title= 'Текущая погода'
    )
    emb.add_field(
        name= 'Температура',
        value= f'{tmp.get("temp")}°'
    )
    emb.add_field(
        name= 'Давление',
        value= str(prs.get('press')) + 'мм рт.ст.'
    )
    emb.add_field(
        name= 'Влажность',
        value= str(hmd) + '%'
    )
    emb.add_field(
        name= 'Облачность',
        value= str(cld) + '%'
    )
    if wnds < 0.2:wnds_str = 'Штиль'
    elif wnds < 1.5: wnds_str = 'Тихий'
    elif wnds < 3.3: wnds_str = 'Лёгкий'
    elif wnds < 5.4: wnds_str = 'Слабый'
    elif wnds < 7.9: wnds_str = 'Умеренный'
    elif wnds < 10.7: wnds_str = 'Свежий'
    elif wnds < 13.8: wnds_str = 'Сильный'
    elif wnds < 17.1: wnds_str = 'Крепкий'
    elif wnds < 20.7: wnds_str = 'Очень крепкий'
    elif wnds < 24.4: wnds_str = 'Шторм'
    elif wnds < 28.4: wnds_str = 'Сильный шторм'
    elif wnds < 32.6: wnds_str = 'Жестокий шторм'
    elif wnds > 32.6: wnds_str = 'Ураган'
    emb.add_field(
        name= 'Степень ветра',
        value= wnds_str
    )
    emb.add_field(
        name= 'Скорость ветра',
        value= str(wnds) + ' м/с'
    )
    emb.set_image(url= w.get_weather_icon_url())
    await ctx.send(embed=emb)




token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
