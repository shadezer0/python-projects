import random
import time

def display_intro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def choose_cave():
    cave = ''
    while cave != '1' and cave !='2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendly_cave = random.randint(1,2)

    if chosen_cave == str(friendly_cave):
        print('Gives you his treasure! Yay!')
    else:
        print('Gobbles you down in one bite! Gulp!')

play_again = 'yes'

while play_again == 'yes' or play_again == 'y':
    display_intro()
    cave_num = choose_cave()
    check_cave(cave_num)
    print('Do you want to play again? (yes or no)')
    play_again = input()
