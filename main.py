import pandas as pd
import edgecalc
import overtime
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("Input both odds: ")
odd1, odd2 = map(int, input().split())
prob = float(input("Input calculated probability: \n"))
ip, edge, houseedge = edgecalc.main(odd1, odd2, prob)
print(f'implied prob is {ip*100}%\nuser edge {edge*100}%\nhouse edge is {houseedge}%')
oddsTaken = int(input("which odds to simulate: "))
total_stack, total_wins, num_bets = overtime.main(prob, oddsTaken)
print(f'{total_stack} here is our final cash total, {(total_wins/num_bets) * 100} here is our win percentage')

