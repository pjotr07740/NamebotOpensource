import discord
from discord.ext import commands
import numpy as np
import os


path = os.path.dirname(os.path.realpath("./swearWords.txt"))

data = np.loadtxt(f'{path}/swearWords.txt', dtype=str, delimiter="\n", encoding="utf8")
bad_words = []

for word in data:
    bad_words.append(word.lower())


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
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
    @commands.has_permissions(view_audit_log=True)
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
    @commands.has_permissions(view_audit_log=True)
    async def scan_all_members(self, ctx, reason=None):
        members = ctx.message.guild.members
        for member in members:
            for bad_word in bad_words:
                if str(member).lower().count(bad_word):
                    await ctx.send(f"{member}'s username has been changed")
                    await member.edit(nick="[NAME REDACTED]", reason=reason)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def purge(self, ctx):
        await ctx.channel.purge(limit=2)

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        await ctx.send(f"Ping is {ping}ms")

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help",
            description="Help on Namebot"
        )
        embed.add_field(name="Bot Developer", value="```load [cog]```\n```unload [cog]```", inline=False)
        embed.add_field(name="Moderators and Bot developer", value="```change_nickname [member] [username] [reason]```\n```remove_username [member] [reason]```\n```scan_all_members [reason]```\n```purge```\n```emshut```", inline=False)
        embed.add_field(name="Public", value="```ping```\n```help```", inline=False)
        await ctx.send(content=None, embed=embed)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def emshut(self, ctx):
        await ctx.send("Shutting down...")
        exit()

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def setup(self, ctx):
        await ctx.send('To get started create a channel named "#logs"! And you are done!')

def setup(bot):
    bot.add_cog(Commands(bot))
