import random
import json
from time import *
import keyboard

# this function is giving paragraph so that user can type it
def load_words():
    with open("general_words.json", "w") as para:
        stories = {
    "words":["This is a modern-day story about a little girl with a big secret she cant tell anyone about. When her teacher finds out her secret, they work together to fix the issue. This story is a good choice for absolute beginners, because it uses only the present tense. Its also written in very basic English with simple vocabulary and short sentences.", "In this story, an old man sets out to ask an African king to dig some wells in his village when their water runs dry. But first, he teaches the king a lesson in humility by showing him how all people help each other. Read the story to see how the clever old man gets the king to do as he asks!",  "This very short story from India was originally written in Sanskrit an ancient language. When a group of doves is caught in a hunters net, they must work together as a team to escape from the hunters clutches. You can listen to a reading of the story as you read along on this website.", "This modern story is about a young woman named Penny who is anxious about going to her familys annual reunion barbecue. But despite screaming children and arguing cousins, Penny ends up happy that she came to the reunion when she starts a conversation with a handsome man. The story is written in simple English, using only the present tense, so its perfect for beginners."]
}
        json.dump(stories, para)
    with open("general_words.json", "r") as para:
        paras = json.load(para)
    
    para_box = paras["words"]
    
    random_num = random.randint(0, len(para_box)-1)
    write_para = para_box[random_num]
    return write_para


# this function is updating leaderboard
def update_leadorboard(word_typed, total_time, wpm):
    with open("leaderboard.json", "w") as leader:
        leader_b = json.dump({"Words Typed":word_typed, "Time Taken":f"{total_time} mins", "Words Per Min": wpm }, leader)


# this function is showing leaderboard
def show_leaderboard():
    with open("leaderboard.json", "r") as leader:
        d = json.load(leader)
    
    for i in d:
        print(f"{i} : {d[i]}")


# this function will show time and speed of typing
def typing_time(initial, end, user_para):
    starting = round(initial, 2)
    ending = round(end, 2)
    total_time_seconds = ending - starting
    total_time_mins = round(total_time_seconds / 60)

    dist = len(user_para)
    times = ending - starting
    speed_wps = dist / times
    speed_wpm = int(speed_wps)  * 60 

    return total_time_mins , speed_wpm

# it takes name of user as input
user_name = input("Enter your name : ")

# here this loop run until user doesn't want to exit from the typing game
while True:
    print("1. Typing Test")
    print("2. Show Leaderboard")
    print("3. Exit")

    if keyboard.is_pressed('ctrl+q'):
        print("Exiting typing")
        print()
        break

    choices = int(input("Choose 1/2/3 : "))
    if choices==1:
        paragraph = load_words()
        print(paragraph)
        start = time()
        print()
        user_input = input("Write : ")
        end = time()
        t_time, speeds = typing_time(start, end, user_input)
        update_leadorboard(len(user_input),t_time, speeds)
        print()
    elif choices==2:
        print(f"{user_name} your leaderboard")
        show_leaderboard()
        print()
    elif choices==3:
        break
    
    else:
        print("Enter valid entry")

print()
print("\t \tWelcome again")
print()