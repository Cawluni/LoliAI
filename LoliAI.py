# Loli AI version 0.2.0
######## IMPORT ########
import discord,loli,requests,urllib,urllib3,lxml,json
from discord.ext import commands
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from lxml import etree


######### VARIABLES ##########
bot_key = loli.bkey
bot = commands.Bot(command_prefix='l!', description='', pm_help=True)
bot.remove_command('help')  # Redefine this.
client = discord.Client()
extensions = ['moderation','nsfw']
players = {}
queue = {}
active_ext = []
#[:-31] ???

## other things ##

### Commands ###
@bot.command(pass_context=True)
async def help(ctx):
  ### Help can give a general help list ###
  await bot.say("Sorry but nothing is functioning right now, Naru is doing a total rewrite of me as we speak! :O")
@bot.command(pass_context=True)
async def cmds(ctx):
  ### Help can give a general help list ###
  await bot.say("Sorry but nothing is functioning right now, Naru is doing a total rewrite of me as we speak! :O")

@bot.command()
async def loaded():
  responce = "Currently have the following modules loaded: {}".format(''.join(active_ext))
  await bot.say(responce)
## Music Things ##


## Moderation ##
@bot.listen()
async def on_message(message):
    print(message.author, ":", message.content, "| said in:", message.channel)
    if message.content == 'fuck you loli':
        await bot.say("No! Fuck you!")

## Other things ##
########

@bot.event
async def on_ready():
    print('[INFO] Loli AI is now running')
    print('[INFO] Version', loli.version)
    await bot.change_presence(game=discord.Game(name='Version: ' + loli.version))
    ## I need to add some more things in terms off saving a servers cog data...##
    # Also I need to be able to 


bot.run(bot_key)
