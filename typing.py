import random
import json
from time import *

def load_words():
    with open("general_words.json", "r") as para:
        paras = json.load(para)
    
    para_box = paras["words"]
    
    random_num = random.randint(0, len(para_box)-1)
    write_para = para_box[random_num]
    return write_para


def update_leadorboard(word_typed, total_time, wpm):
    with open("leaderboard.json", "w") as leader:
        leader_b = json.dump({"Words Typed":word_typed, "Time Taken":total_time, "Words Per Sec": wpm }, leader)

def show_leaderboard():
    with open("leaderboard.json", "r") as leader:
        d = json.load(leader)
    
    for i in d:
        print(f"{i} : {d[i]}")


def typing_time(initial, end, user_para):
    starting = round(initial, 2)
    ending = round(end, 2)
    total_time = ending - starting
    total_time = total_time//60

    dist = len(user_para)
    times = ending - starting
    speed = dist / times
    speed = int(speed) 

    return total_time, speed

    



    
print(load_words())
initial_time = time()
user_input = input("Enter : ")
end_time = time()

total_time, speed = typing_time(initial_time, end_time, user_input)

update_leadorboard(len(user_input), total_time, speed)
show_leaderboard()



    


