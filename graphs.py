
from collections import deque
# ALGORITHM BROAD SEARCH

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_vendor(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    verified = []
    while search_queue:
        person = search_queue.popleft()
        if person not in verified:
            if person_is_vendor(person):
                print(person + " is a mango seller! ")
                return True
            else:
                search_queue += graph[person]
                verified.append(person)
    return False


search("you")
