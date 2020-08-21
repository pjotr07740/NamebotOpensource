import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=".", help_command=None)


@bot.command()
async def load(extension):
    bot.load_extension(f"cogs.{extension}")


@bot.command()
async def unload(extension):
    bot.unload_extension(f"cogs.{extension}")


@bot.event
async def on_ready():
    os.system("clear")
    print(f"Bot loaded! Discord.py Version {discord.__version__}")
    ping = round(bot.latency * 1000)
    print(f"Ping is {ping}ms")
    await bot.change_presence(activity=discord.Streaming(name="Made by Pjotr#1418", url="https://www.twitch.tv/pjotr0707"))

for filename in os.listdir('./cogs'):
    loading = True
    if filename.endswith(".py"):
        print(f"{filename} has been loaded")
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run("NzEyNDE1ODk4MjAzNTg2NTcw.XsRPAg.kCrb_t7i69tTKVTOuVVnJFO-5ck")
