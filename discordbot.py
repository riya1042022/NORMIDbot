import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == 'ping':
        await message.channel.send('pong')
        await message.channel.send(f'Hi {message.author.mention}!')

client.run('MTA4OTgwMjg1NDA4MjAyNzU0MQ.GvbmfU.poczdz7xUTmAtKM5AI2Rt8Xee8wALGNBcaVmlg')
