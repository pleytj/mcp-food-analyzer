# 🧠 MCP Server – Profile Analyzer Tool

This project is a cloud-hosted, MCP-compatible microservice built with FastAPI. It exposes an endpoint that analyzes food products against a user's dietary profile — perfect for use with tools like [n8n](https://n8n.io), chatbots, or health apps.

---

## 🚀 What This Does

This service exposes a single endpoint:

```
POST /mcp/profile_analyzer
```

It receives a structured JSON body containing:
- A user's dietary profile (allergies, diet, health goals, dislikes)
- A list of ingredient IDs
- Nutrition values per 100g

It returns:
- A `score` (0–100)
- `flags` indicating issues (e.g. "contains_peanut", "high_sugar")
- A summary and explanation
- Smart suggestions and product alternatives

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **FastAPI** | Web API framework |
| **Uvicorn** | ASGI server to run FastAPI |
| **Pydantic** | Input/output data validation |
| **GitHub** | Source code management |
| **Railway** | Cloud hosting platform |
| **crewai-tools** *(optional)* | For future multi-agent extensions |

---

## 🔗 Live URLs

| Purpose | URL |
|--------|-----|
| ✅ Swagger UI (Docs/Test Interface) | [https://mcp-food-analyzer-production.up.railway.app/docs](https://mcp-food-analyzer-production.up.railway.app/docs) |
| 📬 API Endpoint | `https://mcp-food-analyzer-production.up.railway.app/mcp/profile_analyzer` |

---

## 🔄 Example Request

```
POST /mcp/profile_analyzer
Content-Type: application/json
```

```json
{
  "user_profile": {
    "allergies": ["peanut"],
    "diet": ["vegan"],
    "dislikes": [],
    "health_goals": ["reduce sugar"]
  },
  "ingredients": [
    { "id": "peanut" },
    { "id": "cocoa" }
  ],
  "nutrition_per_100g": {
    "sugars": 18.0
  }
}
```

---

## 🧠 Why Use MCP?

Using an MCP (Model Control Protocol) structure allows us to:
- Modularize AI tools as callable APIs
- Reuse the same logic across workflows and platforms
- Swap models or prompts without frontend changes
- Scale into more advanced tools later (like GPT-4 Vision or CrewAI agents)

---

## 📁 Project Structure

```
/main.py                   # Starts the FastAPI app
/tools/
  └── profile_analyzer.py  # Core analysis logic
/requirements.txt          # Python dependencies
```

---

## 📝 Next Steps

- Add more tools (e.g., `/mcp/label_reader`)
- Connect this API to n8n workflows
- Add OpenAI integration for GPT-based tools
- Secure endpoint with API key if needed

---
