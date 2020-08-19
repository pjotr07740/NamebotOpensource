import discord
from discord.ext import commands
import numpy as np


data = np.loadtxt(r'C:\Users\pjotr\PycharmProjects\Namebot 2\list.txt', dtype=str, delimiter="\n", encoding="utf8")
bad_words = []

for word in data:
    bad_words.append(word.lower())


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def change_nickname(self, ctx, member: discord.Member = None, username=None, reason=None):

        fail_no_member_provided = discord.Embed(
            title="Oops!",
            description="Something went wrong, please mention the user you want to change!"
        )
        fail_no_member_provided.add_field(name="Exception", value=f"```Missing required argument```")

        fail_changed_author = discord.Embed(
            title="Oops!",
            description="Something went wrong, don't change your own username!"
        )
        fail_changed_author.add_field(name="Exception", value=f"```Blocked.```")

        fail_no_username_provided = discord.Embed(
            title="Oops!",
            description="Something went wrong, please provide a username!",
        )
        fail_no_username_provided.add_field(name="Exception", value=f"```Missing required argument```")

        if member is None:
            await ctx.send(content=None, embed=fail_no_member_provided)
            return

        if member is ctx.message.author:
            await ctx.send(content=None, embed=fail_changed_author)
            return

        if username is None:
            await ctx.send(content=None, embed=fail_no_username_provided)
            return

        successful_embed = discord.Embed(
            title="Username changed",
            description=f"{member.mention}'s username has been changed to {username}"
        )

        await member.edit(nick=username, reason=reason)
        await ctx.send(content=None, embed=successful_embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def remove_username(self, ctx, member: discord.Member = None, reason=None):
        member = member
        reason = reason

        fail_no_member_provided = discord.Embed(
            title="Oops!",
            description="Something went wrong, please mention the user you want to change!"
        )
        fail_no_member_provided.add_field(name="Exception", value=f"```Missing required argument```")

        fail_changed_author = discord.Embed(
            title="Oops!",
            description="Something went wrong, don't change your own username!"
        )
        fail_changed_author.add_field(name="Exception", value=f"```Blocked.```")

        fail_already_no_username = discord.Embed(
            title="Oops!",
            description="Something went wrong, the user already has no username!"
        )
        fail_already_no_username.add_field(name="Exception", value=f"```Blocked.```")

        if member is None:
            await ctx.send(content=None, embed=fail_no_member_provided)
            return

        if member is ctx.message.author:
            await ctx.send(content=None, embed=fail_changed_author)
            return

        if member.nick is None:
            await ctx.send(content=None, embed=fail_already_no_username)
            return

        successful_embed = discord.Embed(
            title="Username changed",
            description=f"{member.mention}'s username has been removed"
        )

        await member.edit(nick=None, reason=reason)
        await ctx.send(content=None, embed=successful_embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def scan_all_members(self, ctx, reason=None):
        members = ctx.message.guild.members
        for member in members:
            for bad_word in bad_words:
                if str(member).lower().count(bad_word):
                    await ctx.send(f"{member}'s username has been changed")
                    await member.edit(nick="[NAME REDACTED]", reason=reason)

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        await ctx.send(f"Ping is {ping}ms")


def setup(bot):
    bot.add_cog(Commands(bot))
