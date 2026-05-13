"""
Written by Rosa Marie Knowles 
Initial Commit: 05/12/2026 
Latest Commit:  05/13/2026

Code to check that the user submitting a command is an admin.
"""

# import needed for type hint
import discord 

async def check_admin(ctx: discord.ApplicationContext) -> bool:
    # user that sent command
    user = ctx.user 

    # iterate through each role 
    # if the role is an admin, return `True`
    for r in user.roles:
        if r.permissions.administrator:
            return True

    # no role is an admin
    return False