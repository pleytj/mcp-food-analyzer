from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crewai_tools.server.fastapi import CrewRouter
from tools.profile_analyzer import analyze_profile

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
router = CrewRouter(tools=[analyze_profile])
app.include_router(router, prefix="/mcp")
