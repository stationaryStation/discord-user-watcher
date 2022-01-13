import discord
from discord.ext import commands
import time

class StatusCog (commands.Cog, name="status"):
    def __init__ (self, bot:commands.bot):
        self.bot = bot

    @commands.command(name = "status",
                    usage="",
                    description="Display the bot's status")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def status(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Ping:")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Ping: `{int(ping)} ms`")

def setup(bot:commands.Bot):
    bot.add_cog(StatusCog(bot))