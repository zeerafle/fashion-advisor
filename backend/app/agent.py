from langgraph.graph import StateGraph, MessagesState, START, END
from typing import TypedDict

class AgentState(TypedDict):
    query: str
    response: str

def process_query(state: AgentState) -> AgentState:
    # Example processing logic
    state['response'] = f"Processed query: {state['query']}"
    return state

def create_agent():
    workflow = StateGraph(AgentState)
    workflow.add_node("process", process_query)
    workflow.set_entry_point("process")
    workflow.set_finish_point("process")
    return workflow.compile()
