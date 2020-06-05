# Your code here
import ntpath

def finder(files, queries):
    cache = {}
    result = []
    for i in queries:
        if i not in cache:
            cache[i] = False
    
    for i in files:
        if ntpath.basename(i) in cache:
            result.append(i)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
