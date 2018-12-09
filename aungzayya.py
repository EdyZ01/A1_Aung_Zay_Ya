
from operator import itemgetter  #importing the itemgetter function from the operator

MENU = "Menu :\n L - List Songs \n A - Add a new song \n C - Complete a song \n Q - Quit" #constants used in the program
MENU_CHOICE = ["a","l", "c", "q"]
LEARNED = "y"
UNLEARNED = "n"
CSV_FILE = "songs.csv"
USER_INPUT = ">>> ".lower()
VERSION = 1.0
NAME = "Aung Zay Ya"

def main():
    print ("Songs To Learn {} - {}".format(VERSION, NAME))
    songs = [] # make a list so that the data from the csv file can be loaded
    load_songs(songs)
    sort_songs(songs)
    print("{} songs loaded".format(len(songs)))
    print(MENU)
    get_menu_choice = input(USER_INPUT)
    get_menu_choice = check_menu_choice(get_menu_choice)
    while get_menu_choice != "q":
        if get_menu_choice == "l":
            sort_songs(songs)
            song_display(songs)
            print(MENU)
            get_menu_choice = input(USER_INPUT)
            get_menu_choice = check_menu_choice(get_menu_choice)
        elif get_menu_choice == "a":
            title = check_title_artist("Title: ")
            artist = check_title_artist("Artist: ")
            year = check_year ("Year: ")
            added_songs = []

            add_new_songs(songs,title,artist,year,added_songs)
            print(MENU)
            get_menu_choice = input(USER_INPUT)
            get_menu_choice = check_menu_choice(get_menu_choice)
        elif get_menu_choice == "c":
            count_song = 0
            for song in range(len(songs)):
                if songs[song][3] == UNLEARNED:
                    count_song += 1  #if the song is not learned yet, it will be counted.
            if count_song == 0:
                print("No more songs to learn") #return a printed status telling that there is no more song to learn.
            else:
                completed_songs(songs)
            print(MENU)
            get_menu_choice = input(USER_INPUT)
            get_menu_choice = check_menu_choice(get_menu_choice)
    sort_songs(songs)
    save_songs(songs)
    print ("{}songs saved to {}".format(len(songs),CSV_FILE))
    print("Thank you for visiting us, have a nice day!")


""" Make a function that will open the songs.csv file and then pass it into the main function
        Then, open the csv file with in file for reading the file
        get title from song file
        get name from song file
        get year from song file
        for line in in_file is reviewed prior to turning into a list
            lines = striped of whitespaces 
            lines = split by commas
            split words = passed into songs list
        close in_file"""

def load_songs(songs): #Read the songs.csv file and append it to the song list.
    read_file = open(CSV_FILE,"r")
    for line in read_file:
        song = line.strip().split(",")
        songs.append(song)
    read_file.close()


def sort_songs(songs): #Sort the songs in the song list by alphabetical order by artist and then by title.
    songs.sort(key=itemgetter(1,0))

def check_menu_choice(menu_choice): #check if the input entered by the user is invalid.
    while menu_choice.lower() not in MENU_CHOICE:
        print("Invalid Menu Choice")
        print(MENU)
        menu_choice= input(USER_INPUT)
    return menu_choice.lower()

def check_title_artist(prompt): #Check whether the input that the user put for the title is blank
    check_input = input(prompt)
    while check_input == "":
        print("The input cannot be leaved as blank")
        check_input = input(prompt)
    return check_input

def check_year(prompt): #Check whether the input that the user put for the year is greater than zero and valid
    check_input = False
    while not check_input:
        try:
            year = int(input(prompt))
            if year >= 0:
                check_input= True
            else:
                print("Number must be great than zero")
                check_input = False
        except ValueError:
            print("Invalid input.Please enter a valid number")
    return year

def add_new_songs(songs, title, artist, year, added_songs): #append the song details that is added by the user into the song list
    added_songs.append(title)
    added_songs.append(artist)
    added_songs.append(str(year))
    added_songs.append(UNLEARNED)
    songs.append(added_songs)
    print("{} by {} ({:>4}) added to song list".format(songs[-1][0], songs[-1][1], songs[-1][2]))

    """Create a function that would mark the song that the user have already learnt in the csv file according to the user's input
    Ask the user to input the number of the song that he wants to learn
    males an error checking function for checking the song choice according to the constants, which is learned and unlearned (in the csv file).
    If the user input is < 0, tell the usedr that the number must be greater than zero.
    if the user input is =LEARNED, tell them that they have already learnt that song
    if the user input is not a number but instead a sting, then error checking function will display as an invalid input
    if the user input is a number which is not in the list, then the error checking system will display a invalid song number
    if the user input is within the list,it will show that the chosen song number is learnt."""

def completed_songs(songs): #the function that worls on the completation part, where the program  check the user input with the no. of songs in the list.
    print("Enter the number of song to be marked as learned")
    check_input = False
    while not check_input:
        try:
            song_choice = int(input(USER_INPUT))
            if song_choice in range(len(songs)) and songs[song_choice][3] !=LEARNED:
                check_input = True
            elif song_choice < 0:
                print("Number must be greater than zero")
            elif songs[song_choice][3] == LEARNED:
                print ("You have already learned {}".format(songs[song_choice][0]))
                return check_input
        except ValueError:
            print("Invalid input,Please input a valid number")
        except IndexError:
            print("Invalid song number")
    songs[song_choice][3]= LEARNED
    print("{} by {} is learned".format(songs[song_choice][0],songs[song_choice][1]))

def song_display(songs):   #will display the list with number of songs which are already learned and which are not learnt yet
    learned = 0
    unlearned = 0
    for song in range(len(songs)):
        if songs[song][3] == UNLEARNED:
            unlearned += 1
            print("{:2}. {} {:25} - {:20} ({:>4})".format(song, "*", songs[song][0], songs[song][1], songs[song][2], songs[song][3]))
        else:
            learned += 1
            print("{:2}. {} {:25} - {:20} ({:>4})".format(song, " ", songs[song][0], songs[song][1], songs[song][2], songs[song][3]))
    print("{} songs are learned, {} songs still need to learn".format(learned, unlearned))

def save_songs(songs):   #saves the songs that we have added into the list and write them on the csv file.
    write_file = open(CSV_FILE ,"w")
    for song in range(len(songs)):
        write_file.write("{},{},{},{}\n".format(songs[song][0], songs[song][1], songs[song][2], songs[song][3]))
    write_file.close()


main()