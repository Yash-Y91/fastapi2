from schema import ReportPayload, ReportResponse
from service.base import GenAIParent
from enums import ServiceName, AnalysisStatus, FailureReason

class ServiceManager:
    @staticmethod
    def generate_report(service_name: ServiceName, report_payload: ReportPayload) -> ReportResponse:
        try:
            service_class = GenAIParent.get_class(service_name)
            # Iterate over the list of transcript entries (user-bot pairs)
            transcript_data = [f"User: {entry.user}, Bot: {entry.bot}" for entry in report_payload.transcript]
            transcript_analytics = service_class().execute(transcript_data)
            return ReportResponse(
                session_id=report_payload.session_id,
                transcript_analytics=transcript_analytics,
                status=AnalysisStatus.SUCCESS
            )
        except ValueError as e:
            return ReportResponse(
                session_id=report_payload.session_id,
                status=AnalysisStatus.FAILURE,
                reason=FailureReason.PROCESSING_ERROR
            )
