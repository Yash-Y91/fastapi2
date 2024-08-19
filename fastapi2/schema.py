from pydantic import BaseModel
from typing import List, Dict, Optional
from enums import AnalysisStatus, FailureReason

class TranscriptEntry(BaseModel):
    user: str
    bot: str

class TranscriptAnalyticsPrompt(BaseModel):
    prompt_id: str
    prompt: str

class ReportPayload(BaseModel):
    session_id: str
    transcript: List[TranscriptEntry]  # Changed to a list of TranscriptEntry dictionaries
    transcript_analytics_prompt: TranscriptAnalyticsPrompt

class ReportResponse(BaseModel):
    session_id: str
    transcript_analytics: Optional[Dict] = None
    status: AnalysisStatus
    reason: Optional[FailureReason] = None
