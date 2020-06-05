def order_pair(pair):
    if pair[0] > pair[1]:
        return pair
    else:
        return pair[::-1]

def get_indices_of_item_weights(weights, length, limit):
    tup = None
    cache = {}
    for i in range(length):
        diff = limit - weights[i]
        if diff in cache:
            tup = order_pair((cache[diff], i))
            break
        cache[weights[i]] = i
    return tup
