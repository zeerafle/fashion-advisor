from fastapi import FastAPI
from app.models import QueryRequest, AgentResponse
from app.agent import create_agent

app = FastAPI()
agent = create_agent()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/query", response_model=AgentResponse)
async def query(request: QueryRequest):
    result = agent.invoke({"query": request.query})
    return AgentResponse(response=result['response'])
