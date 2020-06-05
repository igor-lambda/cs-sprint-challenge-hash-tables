#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    cache = {}
    for t in tickets:
        cache[t.source] = t.destination
    # print(cache)
    route.append(cache['NONE'])
    # print(route)
    for t in range(length):
        # print(route)
        source = route[t]
        dest = cache[source]
        route.append(dest)
        if dest == "NONE":
            break
    print(route)
    return route

