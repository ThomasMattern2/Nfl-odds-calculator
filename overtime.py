import random
import edgecalc

def roll(prob, init_bet, total_stack, num_bets, total_wins, dec_odds):

    if random.random() < prob:
        amount = init_bet * dec_odds - 100  + total_stack
        return amount, total_wins+1, (num_bets + 1)
    else:
        amount = total_stack - init_bet
        return amount , total_wins, (num_bets + 1)

def main(prob, odd1):
    print("Input bet amount and initial coin stack: ")
    init_bet, total_stack = map(int, input().split())
    dec_odds = edgecalc.decimalOdds(odd1)
    i = 0
    num_bets = 0
    total_wins = 0
    while i < 100000:
        total_stack, total_wins, num_bets = roll(prob, init_bet, total_stack, num_bets, total_wins, dec_odds)
        i = i + 1
    return total_stack, total_wins, num_bets