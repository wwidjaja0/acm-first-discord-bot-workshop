import os
import json
import random
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    if bot.user:
        print(f'{bot.user.name} has connected to Discord!')
    try:
        synced = await bot.tree.sync()  # Sync slash commands with Discord
        print(f"Synced {len(synced)} command(s) with Discord.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")


@bot.command(name='hello', help='Responds with a greeting.')
async def old_hello(ctx):
    # this is the deprecated way of doing it
    await ctx.send(f'Hello, {ctx.author.name}!')


@bot.tree.command(name="hello", description="Responds with a greeting.")
async def hello(interaction: discord.Interaction):
    # this is how you should do it
    await interaction.response.send_message(f"Hello, {interaction.user.name}!")


# IMPLEMENT A COMMAND THAT SENDS A RANDOM NUMBER BETWEEN 1 AND 100 HERE


@bot.tree.command(
    name="embed",
    description="Sends a custom embed message with dynamic content.")
@app_commands.describe(
    title="The title of the embed",
    description="The description of the embed",
    color="The color of the embed in hexadecimal (e.g., 0x3498db)")
async def embed(interaction: discord.Interaction, title: str, description: str,
                color: str):
    try:
        embed_color = int(color, 16)  # Convert hex string to integer
        embed = discord.Embed(title=title,
                              description=description,
                              color=embed_color)
        embed.set_footer(text="This is a dynamic embed.")
        await interaction.response.send_message(embed=embed)
    except ValueError:
        await interaction.response.send_message(
            "Invalid color format. Please provide a valid hexadecimal color (e.g., 0x3498db)."
        )


# File to store role message IDs
ROLE_MESSAGE_FILE = "role_message_ids.json"


def load_role_message_ids():
    if os.path.exists(ROLE_MESSAGE_FILE):
        with open(ROLE_MESSAGE_FILE, "r") as file:
            return json.load(file)
    return {}


def save_role_message_ids():
    with open(ROLE_MESSAGE_FILE, "w") as file:
        json.dump(role_message_ids, file)


role_message_ids = load_role_message_ids()  # Load role message IDs on startup


@bot.tree.command(name="create_role_message",
                  description="Creates a message for role assignment.")
@app_commands.describe(
    channel="The channel where the message will be sent.",
    role_name="The name of the role to assign when users react.")
async def create_role_message(interaction: discord.Interaction,
                              channel: discord.TextChannel, role_name: str):
    global role_message_ids

    # Create the role assignment message
    message = await channel.send(f"React with 👍 to get the '{role_name}' role!"
                                 )
    # Store the message ID for the specific server
    role_message_ids[str(interaction.guild_id)] = message.id
    save_role_message_ids()  # Save to file
    await interaction.response.send_message(
        f"Role assignment message created in {channel.mention}!",
        ephemeral=True)


@bot.event
async def on_raw_reaction_add(payload):
    global role_message_ids

    # Check if the reaction is on the specific role assignment message for the server
    if str(
            payload.guild_id
    ) not in role_message_ids or payload.message_id != role_message_ids[str(
            payload.guild_id)]:
        return

    guild = bot.get_guild(payload.guild_id)
    if not guild:
        return

    member = guild.get_member(payload.user_id)
    if not member:
        return

    if payload.emoji.name == '👍':
        # Replace 'Member' with the desired role name
        role = discord.utils.get(guild.roles, name='Member')
        if role:
            await member.add_roles(role)
            print(f"Assigned 'Member' role to {member.name}")


@bot.event
async def on_raw_reaction_remove(payload):
    global role_message_ids

    # Check if the reaction is on the specific role assignment message for the server
    if str(
            payload.guild_id
    ) not in role_message_ids or payload.message_id != role_message_ids[str(
            payload.guild_id)]:
        return

    guild = bot.get_guild(payload.guild_id)
    if not guild:
        return

    member = guild.get_member(payload.user_id)
    if not member:
        return

    if payload.emoji.name == '👍':
        # Replace 'Member' with the desired role name
        role = discord.utils.get(guild.roles, name='Member')
        if role:
            await member.remove_roles(role)
            print(f"Removed 'Member' role from {member.name}")


if TOKEN:
    bot.run(TOKEN)
else:
    print("DISCORD_TOKEN environment variable not found.")
