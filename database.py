import json

class Database():
    def __init__(self, filename):
        self.filename = filename
        try:
            f = open(filename, 'r')
            f.close()
        except FileNotFoundError:
            f = open(filename, 'w')
            json.dump(dict(), f)
            f.close()

    def get_dict(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def save_record(self, record):
        data = self.get_dict()
        current = data.get('record', 0)
        if record > current:
            data['record'] = record
        self.save(data)

    def get_record(self):
        data = self.get_dict()
        return data.get('record', 0)
