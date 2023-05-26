from typing import Optional


class DOMStringMap(dict):
    def __getattr__(self, key) -> Optional[str]:
        try:
            return self[key]
        except KeyError:
            return None

    def __setattr__(self, key, value: str):
        self[key] = str(value)


class Test:

    def __init__(self):
        self._xasd: DOMStringMap = DOMStringMap()

    @property
    def x(self):
        return self._xasd

    @x.setter
    def x(self, val: DOMStringMap):
        self._xasd = val


t = Test()
print(t.x)
t.x = "test"
print(t.x)
