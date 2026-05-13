"""
Written by Rosa Marie Knowles 
Initial Commit: 05/12/2026 
Latest Commit:  05/13/2026

Discord bot for randomly selecting an album for a music club.
"""


# IMPORTS 
from dotenv import load_dotenv
import os 
import discord 
from admincheck import check_admin
# import asyncio


# MAIN
if __name__ == "__main__":
    # get token
    load_dotenv()

    TOKEN = str(os.getenv("TOKEN"))
    ALBUMS_CSV = str(os.getenv("ALBUMS_CSV"))


    # intialize bot 
    bot = discord.Bot()

    # events for when the bot goes online
    @bot.event
    async def on_ready():
        print(f"{bot.user} is online.")
        game = discord.Game("Listening to In The Court of the Green King")
        await bot.change_presence(status=discord.Status.dnd, activity=game)

    """
    # old test command
    @bot.slash_command(name="test", description="testing testing 123")
    async def test(ctx: discord.ApplicationContext):
        await ctx.respond("test command!")
        if (await check_admin(ctx)):
            await ctx.respond("admin.")
        else:
            await ctx.respond("not admin.")
    """

    

    # run the bot 
    bot.run(TOKEN)