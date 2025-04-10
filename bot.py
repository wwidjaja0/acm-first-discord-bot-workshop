import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.messages = True
intents.reactions = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hello', help='Responds with a greeting.')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')


@bot.command(name='ping', help='Responds with Pong!')
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command(name='joke', help='Fetches a random joke.')
async def joke(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://v2.jokeapi.dev/joke/Any') as response:
            if response.status == 200:
                data = await response.json()
                if data.get('type') == 'single':
                    await ctx.send(data['joke'])
                else:
                    await ctx.send(f"{data['setup']} - {data['delivery']}")
            else:
                await ctx.send('Could not fetch a joke at this time.')


@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    if not guild:
        return

    member = guild.get_member(payload.user_id)
    if not member:
        return

    if payload.emoji.name == '👍':
        role = discord.utils.get(guild.roles, name='Member')
        if role:
            await member.add_roles(role)
            print(f"Assigned 'Member' role to {member.name}")


@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    if not guild:
        return

    member = guild.get_member(payload.user_id)
    if not member:
        return

    if payload.emoji.name == '👍':
        role = discord.utils.get(guild.roles, name='Member')
        if role:
            await member.remove_roles(role)
            print(f"Removed 'Member' role from {member.name}")


@bot.command(name='embed', help='Sends a custom embed message.')
async def embed(ctx):
    embed = discord.Embed(
        title="Custom Embed",
        description="This is an example of a custom embed message.",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Field 1", value="This is the value for field 1.", inline=False)
    embed.add_field(
        name="Field 2", value="This is the value for field 2.", inline=False)
    embed.set_footer(text="This is a footer.")
    await ctx.send(embed=embed)


bot.run(TOKEN)
