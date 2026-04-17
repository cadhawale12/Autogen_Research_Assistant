from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

researcher = AssistantAgent(
    name="researcher",
    model_client=OpenAIChatCompletionClient(model="gpt-4o"),
    system_message="You are a research agent. Find detailed information on assigned topics."
)
