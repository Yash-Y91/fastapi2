from fastapi import FastAPI, HTTPException
from enums import ServiceName
from schema import SamplePydantic, ResponsePydanticCSV, ReportPayload, ReportResponse
from service_manager import ServiceManager

app = FastAPI()

@app.post("/analytics", response_model=ResponsePydanticCSV)
async def get_analytics(payload: SamplePydantic):
    return ServiceManager.process_csv(str(payload.url))

@app.post("/genAI/{service_name}/reports", response_model=ReportResponse)
async def generate_report(service_name: ServiceName, report_payload: ReportPayload):
    # Extract CSV data
    csv_data = ServiceManager.process_csv(str(report_payload.transcript_analytics_prompt.prompt))
    
    # Process the report using the appropriate service class
    return await ServiceManager.process_report(service_name, report_payload, csv_data.extracted_data)
