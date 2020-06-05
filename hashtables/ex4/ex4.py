def has_negatives(a):
    result = []
    cache = {}
    sumsies = 0

    positives = [x for x in a if x > 0]
    negatives = [x for x in a if x < 0]

    for i in negatives:
        if i not in cache:
            cache[i] = True
    
    for i in positives:
        if (0 - i) in cache:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
