import csv
import requests
from schema import SamplePydantic, CsvAnalyticsHeader, ReportPayload, ResponsePydanticCSV, ReportResponse
from fastapi import HTTPException
from typing import List
from enums import ServiceName
from service.base import GenAIParent
from io import StringIO


class ServiceManager:
    @staticmethod
    def process_csv(url: str) -> ResponsePydanticCSV:
        # Step 1: Check the file extension
        if not url.endswith('.csv'):
            raise HTTPException(status_code=400, detail="URL does not point to a CSV file")
        
        # Step 2: Download content from the URL
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
        except requests.RequestException as e:
            raise HTTPException(status_code=400, detail=f"Failed to download file: {str(e)}")
        
        # Step 3: Decode and parse the CSV content
        try:
            csv_content = response.content.decode('utf-8')
            csv_reader = csv.reader(StringIO(csv_content))
            headers = next(csv_reader)  # Row 1: Headers
            descriptions = next(csv_reader)  # Row 2: Descriptions
            
            # Validate the CSV format
            if len(headers) != len(descriptions):
                raise HTTPException(status_code=400, detail="CSV format is invalid. Headers and descriptions count do not match.")
            
            extracted_data = [
                CsvAnalyticsHeader(header=h, description=d)
                for h, d in zip(headers, descriptions)
            ]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing CSV: {str(e)}")
        
        return ResponsePydanticCSV(extracted_data=extracted_data)

    @staticmethod
    async def process_report(service_name: ServiceName, payload: ReportPayload, csv_data: List[CsvAnalyticsHeader]) -> ReportResponse:
        try:
            service_class = GenAIParent.get_class(service_name.value)
            response = await service_class().get_analytics(csv_data)
            return response
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
