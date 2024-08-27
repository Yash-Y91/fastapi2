from service.base import GenAIParent
from schema import CsvAnalyticsHeader, ResponsePydanticCSV, ReportResponse
from typing import List
from enums import ServiceName

class Llama(GenAIParent):
    _key = ServiceName.LLAMA

    async def get_analytics(self, data: List[CsvAnalyticsHeader]) -> ReportResponse:
        # Implement the logic to process the analytics using CSV data and transcript
        dummy_analytics = {"tone": "negative", "topics": ["technical support"]}
        return ReportResponse(
            session_id="dummy_session_id",
            transcript_analytics=dummy_analytics,
            status="SUCCESS"
        )