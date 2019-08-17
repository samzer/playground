#!/usr/bin/env python
#title           :Monty Hall with Monte Carlo
#description     :This script uses Monte Carlo simulation on Monty Hall problem
#                 to determine the answer to the Monty Hall problem
#author          : Samir Madhavan
#date            :20190817
#version         :0.1
#usage           :python main.py 10000
#notes           :
#python_version  : >=3.6
#==============================================================================


from random import shuffle, choice
from sys import argv


def monty_hall():
    # Create the doors with random allocation of the car i.e 1
    doors = [0, 1, 0]
    shuffle(doors)

    # Choose a door among the three
    door_selected = choice([0, 1, 2])

    # Open the door that does not have the car
    non_car_doors = list()
    for i,d in enumerate(doors):
        if d == 0 and i != door_selected: non_car_doors.append(i)

    door_opened = choice(non_car_doors)

    # Success if the player does not switch
    non_switch_success =  True if doors[door_selected] == 1 else False

    # Success if the player switches
    remaining_door = set([0,1,2]).difference([door_selected, door_opened])
    remaining_door = remaining_door.pop()
    switch_success =  True if doors[remaining_door] == 1 else False

    return non_switch_success, switch_success


def monte_carlo(n):
    non_switch_success_count = 0
    switch_success_count = 0

    for i in range(n):
        ns, ss = monty_hall()
        non_switch_success_count += ns
        switch_success_count += ss

    print(f"Number of plays: {n}")
    print(f"Number of success on switch: {switch_success_count}  {(switch_success_count/n)*100}%")
    print(f"Number of success on non-switch: {non_switch_success_count}  {(non_switch_success_count/n)*100}%")

N = int(argv[1])
monte_carlo(N)
