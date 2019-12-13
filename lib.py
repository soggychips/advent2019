def get_input(day):
    import json
    with open('input.json', 'rb') as f:
        data = json.loads(f.read())
        return data[str(day)]


def get_input_via_requests(day):
    import os
    if str(day) in os.listdir("input"):
        print("Data for day {} found locally.".format(day))
        text = open("input/{}".format(day), 'r').read()
    else:
        print("Data for day {} not found locally. Downloading...".format(day))
        import requests
        from config import cookies
        url = "https://adventofcode.com/2019/day/{}/input".format(day)
        text = requests.get(url, cookies=cookies).text.strip()
        with open("input/{}".format(day), 'w') as f:
            f.write(text)
    return text.split('\n')


def memoize(f):
    d = {}

    def fun(x):
        if d.get(x) is None:
            d[x] = f(x)
        return d[x]
    return fun
