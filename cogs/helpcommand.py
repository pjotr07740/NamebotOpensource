import discord
from discord.ext import commands

class Embeds:
    #  The general help embed.
    help = discord.Embed(
        title="Help",
        description="All the commands"
    )
    help.add_field(name="General commands", value="\u200b")
    help.add_field(name="This command, the command argument must be without prefix.", value="```.help [command]```", inline=False)
    help.add_field(name="The ping of the bot.", value="```.ping```", inline=False)
    help.add_field(name="How to setup logging for the bot", value="```.setup```", inline=False)
    help.add_field(name="\u200b", value="\u200b", inline=False)
    help.add_field(name="Moderation commands", value="\u200b")
    help.add_field(name="Sets the username of a member.", value="```.change_nickname [member] [new username] [reason]```", inline=False)
    help.add_field(name="Removes the username so it will be set to the default one.", value="```.remove_username [member] [reason]```", inline=False)
    help.add_field(name="Scans all the members in the guild for an offensive username", value="```.scan_all_members [reason]```", inline=False)

    #  Help for the Help command.
    help_help = discord.Embed(
        title="Help for the command Help",
        description="The information for the help command"
    )
    help_help.add_field(name="Base command", value="\u200b")
    help_help.add_field(name="\u200b", value="```.help```", inline=False)
    help_help.add_field(name="Arguments", value="\u200b")
    help_help.add_field(name="Optional", value="```command``` the command you want help with", inline=False)

    #  Help for the Ping command.
    help_ping = discord.Embed(
        title="Help for the command Ping",
        description="The info for the ping command"
    )
    help_ping.add_field(name="Base command", value="\u200b")
    help_ping.add_field(name="\u200b", value="```.ping```", inline=False)

    # Help for the setup command.
    help_setup = discord.Embed(
        title="Help for the command Setup",
        description="The info for the setup command"
    )
    help_setup.add_field(name="Base command", value="\u200b")
    help_setup.add_field(name="\u200b", value="```.setup```", inline=False)

    # Help for the change_nickname command
    help_change_nickname = discord.Embed(
        title="Help for the command change_nickname",
        description="The info for the change_nickname command"
    )
    help_change_nickname.add_field(name="Base command", value="\u200b")
    help_change_nickname.add_field(name="\u200b", value="```.change_nickname```", inline=False)
    help_change_nickname.add_field(name="Arguments", value="\u200b")
    help_change_nickname.add_field(name="Required", value="```member``` ping the member in this argument.", inline=False)
    help_change_nickname.add_field(name="Required", value="```new username``` the new username you want to change it to", inline=False)
    help_change_nickname.add_field(name="Optional", value="```Reason``` the reason why you want to change the nickname", inline=False)

    # Help for the remove_username command
    help_remove_username = discord.Embed(
        title="Help for the command remove_username",
        description="The info for the remove_username command"
    )
    help_remove_username.add_field(name="Base command", value="\u200b")
    help_remove_username.add_field(name="\u200b", value="```.remove_username```", inline=False)
    help_remove_username.add_field(name="Arguments", value="\u200b")
    help_remove_username.add_field(name="Required", value="```member``` ping the member in this argument.", inline=False)
    help_remove_username.add_field(name="Optional", value="```Reason``` the reason why you want to remove the nickname", inline=False)

    # Help for the scan_all_members
    help_scan_all_members = discord.Embed(
        title="Help for the command scan_all_members",
        description="The info for the scan_all_members command"
    )
    help_scan_all_members.add_field(name="Base command", value="\u200b")
    help_scan_all_members.add_field(name="\u200b", value="```.scan_all_members```", inline=False)
    help_scan_all_members.add_field(name="Arguments", value="\u200b")
    help_scan_all_members.add_field(name="Optional", value="```Reason``` the reason why you want to change the nickname", inline=False)


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, command=None):
        #  Normal help command
        if command is None:
            try:
                await ctx.message.author.send(content=None, embed=Embeds.help)
                if not isinstance(ctx.channel, discord.DMChannel):
                    await ctx.send(f"Help embed send in DM's {ctx.message.author.mention}")
            except discord.Forbidden as e:
                await ctx.send(f"I cannot send DM's to you {ctx.message.author.mention}")
                await ctx.send(f"Error:\n```{e}```")
            except Exception as e:
                await ctx.send(f"Error:\n```{e}```")

        #  Help for the help command
        elif command == "help":
            try:
                await ctx.message.author.send(content=None, embed=Embeds.help_help)
                if not isinstance(ctx.channel, discord.DMChannel):
                    await ctx.send(f"Help embed send in DM's {ctx.message.author.mention}")
            except discord.Forbidden as e:
                await ctx.send(f"I cannot send DM's to you {ctx.message.author.mention}")
                await ctx.send(f"Error:\n```{e}```")
            except Exception as e:
                await ctx.send(f"Error:\n```{e}```")

        #  The ping command
        elif command == "ping":
            try:
                await ctx.message.author.send(content=None, embed=Embeds.help_ping)
                if not isinstance(ctx.channel, discord.DMChannel):
                    await ctx.send(f"Help embed send in DM's {ctx.message.author.mention}")
            except discord.Forbidden as e:
                await ctx.send(f"I cannot send DM's to you {ctx.message.author.mention}")
                await ctx.send(f"Error:\n```{e}```")
            except Exception as e:
                await ctx.send(f"Error:\n```{e}```")

        #  The setup command
        elif command == "setup":
            try:
                await ctx.message.author.send(content=None, embed=Embeds.help_setup)
                if not isinstance(ctx.channel, discord.DMChannel):
                    await ctx.send(f"Help embed send in DM's {ctx.message.author.mention}")
            except discord.Forbidden as e:
                await ctx.send(f"I cannot send DM's to you {ctx.message.author.mention}")
                await ctx.send(f"Error:\n```{e}```")
            except Exception as e:
                await ctx.send(f"Error:\n```{e}```")

        elif command == "change_nickname":
            try:
                await ctx.message.author.send(content=None, embed=Embeds.help_change_nickname)
                if not isinstance(ctx.channel, discord.DMChannel):
                    await ctx.send(f"Help embed send in DM's {ctx.message.author.mention}")
            except discord.Forbidden as e:
                await ctx.send(f"I cannot send DM's to you {ctx.message.author.mention}")
                await ctx.send(f"Error:\n```{e}```")
            except Exception as e:
                await ctx.send(f"Error:\n```{e}```")

        elif command == "remove_username":
            try:
                await ctx.message.author.send(content=None, embed=Embeds.help_remove_username)
                if not isinstance(ctx.channel, discord.DMChannel):
                    await ctx.send(f"Help embed send in DM's {ctx.message.author.mention}")
            except discord.Forbidden as e:
                await ctx.send(f"I cannot send DM's to you {ctx.message.author.mention}")
                await ctx.send(f"Error:\n```{e}```")
            except Exception as e:
                await ctx.send(f"Error:\n```{e}```")
def setup(bot):
    bot.add_cog(HelpCommand(bot))