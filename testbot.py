import discord
import os
from discord.ext import commands, tasks
import random
from itertools import cycle
from discord.ext.commands import Bot


client = commands.Bot(command_prefix = ".")

status = cycle(["Wizards101","ToonTown","Club Penguin"])
@client.event
async def on_ready():
    print("I'm READY!")
    #await client.change_presence(status=discord.Status.idle, activity = discord.Game('Wizards101'))
    change_status.start()

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

@client.command(aliases = ['8ball','eightball'])
async def _8ball(ctx, *,question):
    channel = ["my","YouTube","channel","blow","youtube"]
    for x in channel:
        if(channel in question):
            await ctx.send("Definetly not")
            return
    # responses = ["Yes","No","Maybe"]
    # await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')


@client.command(aliases = ['wine','francs'])
async def _wine(ctx, *,question):
    responses = ["One wine mon ami","Oui Oui here is your wine","Fellow Jacque here is your wine"]
    await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount = 3):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member,*,reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.mention}")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {member.mention}')
            return

@client.command()
async def language(ctx,*,profanity):
    bwords = ["frick","shiz"]
    for badword in bwords:
        if(bwords in profanity):
            await ctx.send("watch your language")
            return

    
@tasks.loop(seconds = 15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("invalid command! Please try again")

#client.run(os.environ.get('MendBot_token'))
client.run('NzM4NTA4MjUyMTIzMzY1Mzk5.XyM7aA.FfZrijhPah0wVnfvBayqubFXQJE')