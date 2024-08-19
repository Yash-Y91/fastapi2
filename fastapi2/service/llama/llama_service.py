from service.base import GenAIParent
from enums import ServiceName

class Llama(GenAIParent):
    _key = ServiceName.LLAMA

    def execute(self, transcript_data):
        print(f"Executing Llama with transcript: {transcript_data}")
        # Dummy processing logic for each transcript entry
        return {"tone": "negative", "topics": ["technical support"]}
