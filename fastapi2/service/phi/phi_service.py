from service.base import GenAIParent
from enums import ServiceName

class Phi(GenAIParent):
    _key = ServiceName.PHI

    def execute(self, transcript_data):
        print(f"Executing Phi with transcript: {transcript_data}")
        # Dummy processing logic for each transcript entry
        return {"tone": "positive", "topics": ["account management"]}
