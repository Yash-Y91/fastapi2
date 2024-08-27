from pydantic import BaseModel, HttpUrl
from typing import List, Dict

class CsvAnalyticsHeader(BaseModel):
    header: str
    description: str

class SamplePydantic(BaseModel):
    url: HttpUrl

class TranscriptEntry(BaseModel):
    user: str
    bot: str

class TranscriptAnalyticsPrompt(BaseModel):
    prompt_id: str
    prompt: str

class ReportPayload(BaseModel):
    session_id: str
    transcript: List[TranscriptEntry]
    transcript_analytics_prompt: TranscriptAnalyticsPrompt

class ResponsePydanticCSV(BaseModel):
    extracted_data: List[CsvAnalyticsHeader]

class ReportResponse(BaseModel):
    session_id: str
    transcript_analytics: Dict
    status: str
