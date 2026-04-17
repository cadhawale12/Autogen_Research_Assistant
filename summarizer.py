from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

summarizer = AssistantAgent(
    name="summarizer",
    model_client=OpenAIChatCompletionClient(model="gpt-4o"),
    system_message="You are a summarizer. Create concise, clear summaries of research findings."
)
