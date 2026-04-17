import asyncio
from workflows.research_workflow import run_research

if __name__ == "__main__":
    topic = "Latest trends in Agentic AI"
    result = asyncio.run(run_research(topic))
    print("Final Report:\n", result)
