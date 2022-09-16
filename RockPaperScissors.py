import random

def play():
    user = input("pick: 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r','p','s'])
    print(f"computer chooses {computer}")

    if user == computer :
        return 'Tie'
    if is_win(user,computer):
        return "You Won!"
    return "You Lost!"
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(play())