#Zhiyan Guo

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

import random

class RockPaperScissors:
    choices = ['rock', 'paper', 'scissors']

    def __init__(self, human_players=1):
        self.human_players = human_players
        self.results = {'Player 1': 0, 'Player 2': 0, 'Ties': 0}

    def get_human_choice(self, player_num):
        choice = None
        while choice not in self.choices:
            choice = input(f'Player {player_num}, pick one of rock, paper or scissors: ').lower()
        return choice

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, p1_choice, p2_choice):
        if p1_choice == p2_choice:
            return 'Tie'
        elif (p1_choice == 'rock' and p2_choice == 'scissors') or \
                (p1_choice == 'paper' and p2_choice == 'rock') or \
                (p1_choice == 'scissors' and p2_choice == 'paper'):
            return 'Player 1'
        else:
            return 'Player 2'

    def play_once(self):
        if self.human_players == 0:
            p1_choice = self.get_computer_choice()
            p2_choice = self.get_computer_choice()
        elif self.human_players == 1:
            p1_choice = self.get_human_choice(1)
            p2_choice = self.get_computer_choice()
        else:
            p1_choice = self.get_human_choice(1)
            p2_choice = self.get_human_choice(2)

        print(f'Player 1 chose {p1_choice}')
        print(f'Player 2 chose {p2_choice}')

        winner = self.determine_winner(p1_choice, p2_choice)
        if winner == 'Tie':
            print("It's a tie!")
            self.results['Ties'] += 1
        else:
            print(f'{winner} wins!')
            self.results[winner] += 1

    def play_multiple(self, rounds):
        for _ in range(rounds):
            self.play_once()
        print(f"Results after {rounds} rounds: {self.results}")

game = RockPaperScissors(human_players=1)
game.play_once()

rounds = int(input('How many rounds would you like to play? '))
game.play_multiple(rounds)