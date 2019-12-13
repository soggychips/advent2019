def get_input(day):
    import json
    with open('input.json', 'rb') as f:
        data = json.loads(f.read())
        return data[str(day)]


def memoize(f):
    d = {}

    def fun(x):
        if d.get(x) is None:
            d[x] = f(x)
        return d[x]
    return fun
