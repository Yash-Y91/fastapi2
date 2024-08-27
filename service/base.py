from schema import CsvAnalyticsHeader, ReportPayload, ReportResponse
from typing import List, Dict

class GenAIParent:
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, '_key') or cls._key is None:
            raise ValueError(f"Subclasses of {cls.__name__} must define a 'key' when inheriting")
        if cls._key in cls._registry:
            raise ValueError(f"Key {cls._key} already exists in registry")
        cls._registry[cls._key] = cls
        print(f"Registered subclass {cls.__name__} with key {cls._key}")

    @classmethod
    def get_class(cls, key):
        if key not in cls._registry:
            raise ValueError(f'Key {key} not found in registry')
        return cls._registry[key]

    async def get_analytics(self, data: List[CsvAnalyticsHeader]) -> ReportResponse:
        raise NotImplementedError("Subclasses must implement this method")
