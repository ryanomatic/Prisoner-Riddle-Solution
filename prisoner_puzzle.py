import random

def play_game(prisoner_count = 100):
    # create list of 100 objects to insert into boxes randomly
    insert_numbers = [i for i in range(0,prisoner_count)]
    boxes = []

    while len(insert_numbers) > 0:
        pick = random.randrange(0,len(insert_numbers))
        boxes.append(insert_numbers.pop(pick))

    # create list of 'prisoners' and have them select their own number and follow it's path
    # limit 'prisoner' to guessing only half of the total boxes

    guesses = int(prisoner_count / 2)
    prisoners = [i for i in range(0,prisoner_count)]

    for prisoner in prisoners:
        saved = False
        box_to_find = prisoner #set initial box to find
        for guess in range(guesses):
            number_found = boxes[box_to_find]
            if number_found == prisoner:
                saved = True
                break #Saved! Exit this loop and try the next prisoner
            else:
                box_to_find = number_found # No luck, try again if there are guesses remaining
        if saved == False:
            #print("Lose")
            return 0
    
    #print("Win")
    return 1

games_to_play = 1000
win_count = 0
for i in range(games_to_play):
    win_count += play_game()

print("Total wins:",win_count,"Total games:",games_to_play)