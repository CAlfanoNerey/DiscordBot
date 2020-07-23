import discord
import os
from discord.ext import commands
import random
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("I'm READY!")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has been sent to the gulag!')

@client.command(aliases = ['magicconch','conch'])
async def _mconch(ctx, *,question):
    responses = ["Yes","No","Maybe"]
    await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount = 3):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    
client.run(os.environ.get('MendBot_token'))