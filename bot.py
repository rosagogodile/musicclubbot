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

def default_admin_response(command_name:str) -> str:
    return f"Only users with Administrator privileges are able to run ***{command_name}***."

# MAIN
if __name__ == "__main__":
    # get token
    load_dotenv()

    TOKEN = str(os.getenv("TOKEN"))
    ALBUMS_CSV = str(os.getenv("ALBUM_CSV"))
    # role that bot will tag when it needs to notify entire server
    ROLE = str(os.getenv("ROLE"))
    # thumbnail for embeds 
    THUMB = str(os.getenv("THUMB"))

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
        # only allow admins to run this command 
        if (await check_admin(ctx)):
            chosen_album = await pick_album(ALBUMS_CSV)
            # await ctx.respond(await ltostr(chosen_album))

            # case if no albums are remaining
            if chosen_album is None:
                await ctx.respond(f"There are no albums remaining! Please update *{ALBUMS_CSV}* with more albums to continue.")
                return

            # build embed 

            embed = discord.Embed(
                title="Album of the Week",
                description="",
                color=discord.Colour.from_rgb(0,255,0)
            )

            embed.add_field(name="Album Title:", value=chosen_album[1], inline=False)
            embed.add_field(name="Artist:", value=chosen_album[0], inline=False)
            embed.add_field(name="Date Released:", value=chosen_album[2], inline=False)

            # adds genres to embed 
            # changes field to be plural if there are more than one genres 
            # removes the last 2 characters of the genre embed since they are a trailing comma and whitespace
            genres = await ltostr(chosen_album[3], ", ")
            embed.add_field(name="Genres:" if len(chosen_album) > 1 else "Genre:", value=genres[:-2], inline=False)

            embed.set_author(name="Album Chud", icon_url=THUMB)
            embed.set_thumbnail(url=THUMB)
            embed.set_image(url=chosen_album[4])

            await ctx.respond(ROLE, embed=embed)
        else:
            # user that isn't an admin tries to run this command 
            await ctx.respond(default_admin_response("Album"))
        



    # events for when the bot goes online
    @bot.event
    async def on_ready():
        print(f"{bot.user} is online.")
        game = discord.Game("Listening to In The Court of the Green King")
        await bot.change_presence(status=discord.Status.dnd, activity=game)

    # run the bot 
    bot.run(TOKEN)