#!/usr/bin/env python3

def basic_graph():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    return graph

def weighted_graph():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}

    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = float("inf")

    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    return graph, costs, parents