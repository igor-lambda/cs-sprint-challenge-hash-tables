def intersection(arrays):
    cache = {}
    length = len(arrays)
    result = []
    for sublist in arrays:
        for item in sublist:
            if item not in cache:
                cache[item] = 1
            else:
                cache[item] += 1
    
    for key, val in cache.items():
        if val >= length:
            result.append(key)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
