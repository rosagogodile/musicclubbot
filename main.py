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

    token = str(os.getenv("TOKEN"))
    print(token)