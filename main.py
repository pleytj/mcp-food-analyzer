from fastapi import FastAPI
from tools.profile_analyzer import analyze_profile, ProfileAnalyzerInput
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (for n8n or frontend use)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/mcp/profile_analyzer")
def run_profile_analyzer(input_data: ProfileAnalyzerInput):
    return analyze_profile(input_data)
