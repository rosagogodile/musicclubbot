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
from albumpicker import *

# MAIN
if __name__ == "__main__":
    # get token
    load_dotenv()

    TOKEN = str(os.getenv("TOKEN"))
    ALBUMS_CSV = str(os.getenv("ALBUM_CSV"))

    # intialize bot 
    bot = discord.Bot()

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
    

    @bot.slash_command(name="album", description="Admin Only: Pick an Album For The Next Meeting.")
    async def album(ctx: discord.ApplicationContext):
        chosen_album = await pick_album(ALBUMS_CSV)
        await ctx.respond(await ltostr(chosen_album))


    # events for when the bot goes online
    @bot.event
    async def on_ready():
        print(f"{bot.user} is online.")
        game = discord.Game("Listening to In The Court of the Green King")
        await bot.change_presence(status=discord.Status.dnd, activity=game)

    # run the bot 
    bot.run(TOKEN)