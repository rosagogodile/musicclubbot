"""
Written by Rosa Marie Knowles 
Initial Commit: 05/12/2026 
Latest Commit:  05/12/2026

Discord bot for randomly selecting an album for a music club.
"""


# IMPORTS 
from dotenv import load_dotenv
import os 
import discord 

# MAIN
if __name__ == "__main__":
    # get token
    load_dotenv()

    TOKEN = str(os.getenv("TOKEN"))


    # intialize bot 
    bot = discord.Bot()

    # prints when the bot is online 
    # useful for debugging?
    @bot.event
    async def on_ready():
        print(f"{bot.user} is online.")

    @bot.slash_command(name="test", description="testing testing 123")
    async def test(ctx: discord.ApplicationContext):
        await ctx.respond("test command!")
        await ctx.respond(str(ctx.user))

    # run the bot 
    bot.run(TOKEN)