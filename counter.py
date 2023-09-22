import os

list = open("data.txt", "r").readlines()

no = list.count('0\n')
si = list.count("1\n")
total = len(list)
print(f"\nyou have failed {no} days and you win {si} days!")
si_percent = str(si/total)
no_percent = str(no/total)
print(f"\nthe percent of si is {si_percent[0:4]}%")
print(f"the percent of no is {no_percent[0:4]}%")
print("\n-----------------------------------")
print(f"\nsi : {si_percent}%")
print(f"no : {no_percent}%")
print("\n")
