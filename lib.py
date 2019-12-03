def get_input(day):
    import json
    with open('input.json', 'rb') as f:
        data = json.loads(f.read())
        return data[str(day)]
