autogen-research-assistant/
│
├── requirements.txt        # Dependencies
├── config/                 # API keys, model configs
│   └── openai_config.json
├── agents/                 # Agent definitions
│   ├── researcher.py
│   └── summarizer.py
├── workflows/              # Multi-agent orchestration
│   └── research_workflow.py
├── app.py                  # Entry point
└── Dockerfile              # For deployment
