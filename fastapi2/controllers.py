from fastapi import FastAPI, HTTPException
from schema import ReportPayload, ReportResponse
from enums import ServiceName
from service_manager import ServiceManager

app = FastAPI()

@app.post("/genAI/{service_name}/reports", response_model=ReportResponse)
async def generate_report(service_name: ServiceName, report_payload: ReportPayload):
    return ServiceManager.generate_report(service_name, report_payload)
