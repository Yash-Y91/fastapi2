from service.base import GenAIParent
from enums import ServiceName

class OpenAI(GenAIParent):
    _key = ServiceName.OPENAI

    def execute(self, transcript_data):
        print(f"Executing OpenAI with transcript: {transcript_data}")
        # Dummy processing logic for each transcript entry
        return {"tone": "neutral", "topics": ["order support"]}
