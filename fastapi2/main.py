import uvicorn
from controllers import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


# {
#     "session_id": "12345",
#     "transcript": {
#         "user": "I need help with my order",
#         "bot": "Sure, can you provide your order number?"
#     },
#     "transcript_analytics_prompt": {
#         "prompt_id": "001",
#         "prompt": "Analyze the tone and topics of this conversation."
#     }
# }
