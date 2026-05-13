"""
Written by Rosa Marie Knowles 
Initial Commit: 05/13/2026 
Latest Commit:  05/13/2026

Code to pick an album from a csv file
"""

# IMPORTS 
import csv
import asyncio
import aiofiles
from io import StringIO
import random
from datetime import datetime

DATE_INDEX = 2
GENRE_INDEX = 3

# function that recursively converts a list into a string 
# used for testing, and not much else! 
async def ltostr(a: list) -> str:
    if isinstance(a, list) == False:
        # or used to convert `None` to empty string
        return str(a) or ""

    output = ""

    for i in a:
        if isinstance(i, list) == False:
            output += f"{str(i)} "
        else:
            output += f"{await ltostr(i)} "

    return output

# function that picks an album
async def pick_album(filename: str) -> list:

    # list that contains file contents 
    albums = []

    async with aiofiles.open(filename, "r", encoding="utf-8") as acsv:
        file_contents = await acsv.read()
        # set up csv reader 
        csvreader = csv.reader(StringIO(file_contents))

        for row in csvreader:
            albums.append(row)

    # find the index values of all available albums
    available_index = []
    for i in range(len(albums)):
        if (albums[i][-2] != "1"):
            available_index.append(i)

    # case where there are no available index values 
    if (len(available_index) < 1):
        return None

    # mark last played album as no longer being weekly pick 
    for i in range(len(albums)):
        if (albums[i][-1] == "1"):
            albums[i][-1] = "0"

    # index of chosen album
    idx = random.choice(available_index)
    # update boolean for if the album is the current weekly pick
    albums[idx][-1] = "1"
    # update boolean for if the album has currently been picked 
    albums[idx][-2] = "1"

    # write new album contents to file 
    async with aiofiles.open(filename, "w", encoding="utf-8") as acsv:
        file_contents = ""

        # convert list of album lists into a csv format
        for a in albums:
            for i in a:
                file_contents += f"{i},"

            # remove trailing comma
            file_contents = file_contents[:-1]
            file_contents += "\n"

        # remove trailing newline
        file_contents = file_contents[:-1]

        await acsv.write(file_contents)

    rtrnval = albums[idx]

    # update date format 
    temp = rtrnval[DATE_INDEX].split("/")
    # year, month, day
    new_date = datetime(int(temp[2]), int(temp[0]), int(temp[1]))
    rtrnval[DATE_INDEX] = new_date.strftime("%B %d, %Y")

    # convert genres into a list of genres 
    rtrnval[GENRE_INDEX] = rtrnval[GENRE_INDEX].split("|")

    return rtrnval