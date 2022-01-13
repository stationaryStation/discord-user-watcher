import discord
from discord.ext import commands
from profanity import has_profanity
from profanity_filter import ProfanityFilter

pf = ProfanityFilter()


class WatcherCog(commands.Cog, name="watching"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if has_profanity(message.content):
            await message.delete()
            print("Message detected and deleted.")
        elif pf.is_profane(message.content):
            await message.delete()
            print("message detected and deleted.")


def setup(bot):
    bot.add_cog(WatcherCog(bot))
