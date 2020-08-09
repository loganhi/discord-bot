# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '.')

@client.command()
async def clear(ctx, amount=1):
    print(ctx.author.top_role)
    if str(ctx.author.top_role) == "Admin":
        try:
            await ctx.channel.purge(limit=amount)
        except Exception as error:
            print(error)
    else:
        await ctx.send("You aren't an Admin")
@client.command()
async def ping(ctx):
    await ctx.send('Pong')

@client.event
async def on_message(ctx):
    # we do not want the bot to reply to itself
    command = ctx.content.lower()
    if ctx.author == client.user:
        return

    if 'the' in command:
        msg = 'I am TODD {0.author.mention}'.format(ctx)
        await ctx.channel.send(msg)
    
    await client.process_commands(ctx)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)