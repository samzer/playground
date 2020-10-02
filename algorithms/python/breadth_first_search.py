#!/usr/bin/env python3
from data import basic_graph
from collections import deque

graph_data = basic_graph()
search_deque = deque()

search_deque += graph_data
searched = []

def person_is_seller(name):
    return name[-1] == 'm'

while search_deque:
    entity = search_deque.popleft()
    if person_is_seller(entity):
        print(f"{entity} is a seller")
        break
    else:
        search_deque += graph_data[entity]
        searched.append(entity)
    

