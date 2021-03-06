import discord
from discord.ext import commands
import asyncio
import os


path = os.path.dirname(os.path.realpath("./swearWords.txt"))

data = open("swearWords.txt", "r")
bad_words = []


for word in data:
    bad_words.append(word.lower())


class AutoCensor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        username_change_bot = discord.Embed(
            title="Username changed",
            description="Namebot changed a username"
        )

        username_change_user = discord.Embed(
            title="Username changed",
            description="Someone changed his/her username"
        )

        guild = after.guild
        channel = discord.utils.get(guild.text_channels, name="logs")
        try:
            nick = after.nick.lower()
        except Exception as e:
            nick = None
        if nick is not None:
            for bad_word in bad_words:
                if nick.count(bad_word) > 0:
                    username_change_bot.add_field(name="User", value=f"```{after}```")
                    try:
                        await after.edit(nick="[NAME REDACTED]", reason="Auto change")
                    except:
                        pass
                    finally:
                        try:
                            await channel.send(content=None, embed=username_change_bot)
                        except:
                            print("Logging failed...")
                    return

        await asyncio.sleep(10)
        if nick is not None:
            for bad_word in bad_words:
                if not nick.find(bad_word):
                    username_change_user.add_field(name="User", value=f"```{after}```")
                    username_change_user.add_field(name="New username", value=f"```{nick}```")
                    await channel.send(content=None, embed=username_change_user)
                    return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        username_change_bot = discord.Embed(
            title="Username changed",
            description="Namebot changed a username"
        )

        username_change_user = discord.Embed(
            title="Username changed",
            description="Someone changed his/her username"
        )

        guild = member.guild
        channel = discord.utils.get(guild.text_channels, name="logs")

        try:
            nick = member.nick.lower()
        except Exception as e:
            nick = None

        if nick is not None:
            for bad_word in bad_words:
                if nick.count(bad_word) > 0:
                    username_change_bot.add_field(name="User", value=f"```{member}```")
                    try:
                        await member.edit(nick="[NAME REDACTED]", reason="Auto change")
                    except:
                        pass
                    finally:
                        await channel.send(content=None, embed=username_change_bot)
                    return

        await asyncio.sleep(10)
        if nick is not None:
            for bad_word in bad_words:
                if not nick.find(bad_word):
                    username_change_user.add_field(name="User", value=f"```{member}```")
                    username_change_user.add_field(name="New username", value=f"```{member}```")
                    await channel.send(content=None, embed=username_change_user)
                    return


def setup(bot):
    """
    :param bot: a discord.client
    :return: None
    """
    bot.add_cog(AutoCensor(bot))
