from enums import ServiceName, AnalysisStatus, FailureReason
from schema import ReportPayload, ReportResponse

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

    @property
    def key(self):
        return self._key

    @classmethod
    def get_class(cls, key):
        if key not in cls._registry:
            raise ValueError(f'Key {key} not found in registry')
        return cls._registry[key]

    def execute(self, payload):
        raise NotImplementedError("Subclasses must implement this method")
