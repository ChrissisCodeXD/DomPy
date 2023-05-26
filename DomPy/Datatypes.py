from typing import Optional

class DOMStringMap(dict):
    def __getattr__(self, key) -> Optional[str]:
        try:
            return self[key]
        except KeyError:
            return None

    def __setattr__(self, key, value: str):
        self[key] = str(value)
