import time
from typing import Dict, Any

class StateStore:
    def __init__(self):
        self._state: Dict[str, Dict[str, Any]] = {}

    def write(self, key: str, value: Any):
        self._state[key] = {
            "value": value,
            "timestamp": time.time()
        }

    def read(self, key: str):
        return self._state.get(key, {}).get("value")

    def snapshot(self):
        return self._state.copy()
