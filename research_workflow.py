import asyncio
from agents.researcher import researcher
from agents.summarizer import summarizer

async def run_research(topic):
    research_output = await researcher.run(task=f"Research {topic}")
    summary_output = await summarizer.run(task=f"Summarize: {research_output}")
    return summary_output
