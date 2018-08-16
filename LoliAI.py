 # version 0.1.6
import loli, discord, time, random # Time is just used for a timeout.
from discord.ext import commands

bot_key = loli.bkey
bot = commands.Bot(command_prefix='l!',description='',pm_help=True)
bot.remove_command('help') #Redefine this.
client = discord.Client()
help = loli.help
players = {}
queue = {}
def check_queue(id):
    if queue[id] != []:
        players = queue[id].pop(0)
        players[id] = players
        players.start()

@bot.listen()
async def on_message(message):
    print(message.author, ":", message.content, "| said in:", message.channel)

@bot.command()
async def cmds():
    coms = loli.commands
    await bot.say(coms)

@bot.command(pass_context=True)
async def play(ctx, *, url):
    msg = ctx.message
    channel = msg.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = msg.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def play(ctx, *, url):
    m = ctx.message
    if 'https://youtube.com/' in m:
        msg = ctx.message
        channel = msg.author.voice.voice_channel
        await bot.join_voice_channel(channel)
        server = msg.server
        voice_client = bot.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        players[server.id] = player
        player.start()
    else:
        msg = ctx.message
        

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

@bot.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@bot.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@bot.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    if server.id in queue:
        queue[server.id].append(player)
    else:
        queue[server.id] = [player]
    await bot.say("Video was added to queue")

@bot.command(pass_context=True)
async def gay(ctx):
    url = "https://www.youtube.com/watch?v=hGA-Qid-ChI"
    msg = ctx.message
    channel = msg.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = msg.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def communisumlove(ctx):
    url = "https://www.youtube.com/watch?v=U06jlgpMtQs"
    msg = ctx.message
    channel = msg.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = msg.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


@bot.command(pass_context=True)
async def youtube(ctx):
    url = "https://www.youtube.com/watch?v=brNGDA5R048"
    msg = ctx.message
    channel = msg.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = msg.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def loliporn(ctx):
    url = "https://www.youtube.com/watch?v=LO1Z8HOGeWo"
    msg = ctx.message
    channel = msg.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = msg.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def brotherscock(ctx):
    url = "https://www.youtube.com/watch?v=TBA7Hjch4tY"
    msg = ctx.message
    channel = msg.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = msg.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def ilikemen(ctx):
    url = "https://www.youtube.com/watch?v=NYg96m-7rPA"
    msg = ctx.message
    channel = msg.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = msg.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


@bot.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@bot.command()
async def invite():
    await bot.say(
        "Y-You are inviting me!?!?!! E-Eh-EHHH!?!.....W-Well if you insist...: https://discordapp.com/api/oauth2/authorize?client_id=408817025876623361&permissions=8&scope=bot")

@bot.event
async def on_ready():
    print('[INFO]]Loli AI is now running')
    print('[INFO] Version',loli.version)
    await bot.change_presence(game=discord.Game(name='Version: '+loli.version))

@bot.command(pass_context=True)
async def volume(ctx, volume):
    await bot.say('You just got pranked! I cant do this yet :D')

## REDO EVERYHTHING MUSIC BASED IN ONE AREA/SECTION OR A SEPERATE SCRIPT!
# Its to cluttered ;-;
bot.run(bot_key)
