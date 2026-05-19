"""
Written by Rosa Marie Knowles 
Initial Commit: 05/13/2026 
Latest Commit:  05/19/2026

Script for managing the csv file containing the albums 
"""

# IMPORTS 
from dotenv import load_dotenv
import csv
import os

# replaces commas with a hardcoded placeholder character 
# allows csv files to contain strings with commas in them without breaking
def mod_comma(i:str) -> str:
    return i.replace(",", "∘")

# helper function, shouldn't be called by user
def update_file(contents: list, filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as f: 
        file_contents = ""

        # convert list of albums into csv format 
        for c in contents: 
            for d in c: 
                file_contents += f"{d},"

            # remove trailing comma 
            file_contents = file_contents[:-1]
            file_contents += "\n"

        # remove trailing newline 
        file_contents = file_contents[:-1]

        f.write(file_contents)

# marks each album as being unlistened 
# useful for testing the bot 
def reset(contents: list, filepath: str) -> list:
    for i in range(len(contents)):
        contents[i][-1] = "0"
        contents[i][-2] = "0"

    update_file(contents, filepath)

    return contents

# command to add an album 
def add_album(contents: list, filepath: str) -> list: 
    new_album = []

    new_album.append(mod_comma(input("Artist name: ").strip()))
    new_album.append(mod_comma(input("Album name: ").strip()))
    new_album.append(mod_comma(input("Release Date (mm/dd/yyyy): ").strip()))

    # loop and allow user to add multiple genres 
    looping = True
    genres = []
    while looping: 
        choice = mod_comma(input("Add Genre (q to exit loop): ").strip())
        if choice == "q":
            looping = False
        else:
            genres.append(choice)

    genres_str = ""
    for g in genres:
        genres_str += f"{g}|"

    # remove trailing bar 
    genres_str = genres_str[:-1]

    new_album.append(genres_str)
    # don't need to call `mod_comma` here since an image link shouldn't have a comma in it 
    new_album.append(input("Album Cover Link: ").strip())

    # append booleans used to check if album has been listened to 
    for i in range(2):
        new_album.append("0")

    contents.append(new_album)
    update_file(contents, filepath)
    return contents


command_map = {
    "reset": reset,
    "addalbum": add_album
}

# MAIN
if __name__ == "__main__":
    # get csv filepath
    load_dotenv()
    filepath = str(os.getenv("ALBUM_CSV"))

    # read csv file 
    contents = []
    with open(filepath, "r", encoding="utf-8") as f:
        csvfile = csv.reader(f)
        for r in csvfile:
            contents.append(r)

    # for r in contents:
    #     for j in r:
    #         print(j)
    #     print("")

    looping = True 

    # program loop
    while looping: 
        command = input("Enter command: ").strip().lower()

        # exit 
        if command == "quit":
            looping = False
        elif command in command_map: 
            contents = command_map[command](contents, filepath)
        else:
            print(f"Command \"{command}\" not found.")
            