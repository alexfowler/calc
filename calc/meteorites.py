import json
import urllib.request

from calc import calc

URL = "https://data.nasa.gov/resources/y77d-th95.json"


class MeteoriteStats:

    def get_data(self):
        with urllib.request.urlopen(URL) as url:
            data = json.loads(url.read().decode())

    def average_mass(self, data):
        c = calc.Calc()
        masses = [float(d['mass']) for d in data if 'mass' in d]

        return c.avg(masses)

