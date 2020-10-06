#!/usr/bin/env python3
from data import weighted_graph

def dijkstras():
    graph, costs, parents = weighted_graph()
    processed = []

    def find_cheapest_node():
        cheapest_node = None
        cheapest_node_value = float("inf")

        for n in costs.keys():
            if costs[n] < cheapest_node_value and n not in processed:
                cheapest_node = n
                cheapest_node_value = costs[n]
        
        return cheapest_node


    node = find_cheapest_node()
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]

        for neighbour in neighbours.keys():
            new_cost = cost + neighbours[neighbour]
            if costs[neighbour] > new_cost:
                costs[neighbour] = new_cost
                parents[neighbour] = node
        
        processed.append(node)
        node = find_cheapest_node()
        print(node)

    print("---Costs----")
    print(costs)

    print("---Parents---")
    print(parents)

dijkstras()