# 🛠️ SETUP.md – Project Log: MCP Server Deployment

This document outlines all the steps taken to create, deploy, and validate a cloud-hosted MCP (Model Control Protocol) server for food profile analysis. The service is now publicly accessible and integrated with external tools such as n8n.

---

## 🎯 Goal

Create a modular, cloud-hosted microservice for analyzing food products against a user’s dietary profile. The service should follow the MCP pattern and be usable from external tools via a REST API.

---

## ✅ Step-by-Step Setup Process

### 📁 Project Creation & Local Setup

- Downloaded a pre-built ZIP project containing:
  - `main.py` – FastAPI app definition
  - `tools/profile_analyzer.py` – logic and schemas
  - `requirements.txt` – Python dependencies
- Confirmed profile analyzer used Pydantic and no external dependencies

---

### 🐙 GitHub Setup

- Created a new GitHub account and repository (`mcp-food-analyzer`)
- Uploaded the project files:
  - `main.py`
  - `tools/profile_analyzer.py`
  - `tools/__init__.py`
  - `requirements.txt`
- Deleted mistakenly uploaded `tools` as a file and re-uploaded it correctly as a folder

---

### ☁️ Railway Deployment

- Created a Railway account
- Connected GitHub to Railway
- Deployed project using "Deploy from GitHub"
- Railway automatically built and ran the container

---

### ⚠️ Debugging & Fixes

- ❌ App crash: missing start command → fixed by adding:
  ```
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```
- ❌ Import errors:
  - Changed to relative import: `from .tools.profile_analyzer import ...`
  - Added `__init__.py` in root to make it a package
- ❌ Port mismatch → confirmed service runs on port `8000`
- ❌ Wrong URL used (`/mcp/.../docs`) → corrected to `/docs`

---

### 🌍 Domain Exposure

- Exposed Railway service publicly
- Verified final domain:
  - Swagger: `https://mcp-food-analyzer-production.up.railway.app/docs`
  - Endpoint: `https://mcp-food-analyzer-production.up.railway.app/mcp/profile_analyzer`

---

## 🔗 Integration Ready

- Tested in Swagger with sample input
- Connected to n8n via HTTP POST
- Returns structured score, flags, and suggestions

---

## 📦 Final Deliverables

- ✅ Live microservice hosted on Railway
- ✅ GitHub repo with all logic and dependencies
- ✅ Swagger UI for easy testing
- ✅ Clean README.md
- ✅ This `SETUP.md` for audit and reuse

---

