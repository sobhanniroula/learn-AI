# AI Agents Course (Hugging Face)

Course 3 of my [learn-AI](../README.md) path.

**Course:** [AI Agents Course (Hugging Face)](https://huggingface.co/learn/agents-course/unit0/introduction)

**Status:** In progress

## About the course

A free, self-paced course that takes you from beginner to expert in understanding, using and building AI agents. It mixes theory with hands-on practice using established agent libraries, and ends with building agents for real-world use cases and a benchmark-based final challenge.

- **Prerequisites:** basic Python, basic LLM knowledge (a refresher is given in Unit 1), and a free Hugging Face account
- **Time:** about 3–4 hours per week, designed to be done one unit per week; there is no deadline
- **Frameworks covered:** smolagents, LangGraph, LlamaIndex

## Syllabus

| Unit | Topic | What it covers |
| ---- | ----- | -------------- |
| 0 | Onboarding | Setting up the tools and platform |
| 1 | Agent fundamentals | Tools, thoughts, actions, observations, LLMs and messages |
| 2 | Frameworks | Building agents with smolagents, LangGraph and LlamaIndex |
| 3 | Use cases | Real-world agent applications |
| 4 | Final assignment | Building an agent and evaluating it on a benchmark, with a public leaderboard |
| Bonus | Extra units | Fine-tuning LLMs for function-calling, agent observability and evaluation, and building agents for Pokémon battles |

## Certificates

The course offers two free certificates:

- **Fundamentals Certificate:** complete Unit 1
- **Completion Certificate:** complete Unit 1, one use-case assignment, and the final challenge

## Projects

Each unit is a folder, and each project of that unit is a subfolder inside it. Projects are added as I complete them.

```
3-ai-agents-course/
└── unit-1-introduction-to-agents/
    ├── project-1-dummy-agent-library/       # Completed
    └── project-2-agent-using-smolagents/    # Not started
```

### Unit 1: Introduction to Agents — [`unit-1-introduction-to-agents/`](unit-1-introduction-to-agents)

**Status:** In progress

#### Project 1: Dummy Agent Library — [`project-1-dummy-agent-library/`](unit-1-introduction-to-agents/project-1-dummy-agent-library)

A notebook that builds an agent from scratch, without a framework, using a local `qwen2:7b` model served by Ollama.

**How it works**

1. A ReAct-style system prompt describes one tool, `get_weather`, and forces the Thought / Action (JSON) / Observation format.
2. Generation is stopped at `Observation:` so the model cannot hallucinate the tool result.
3. The code runs the dummy `get_weather` function with the model's chosen arguments.
4. The result is appended as an Observation, and the model returns the final answer.

**Tech stack**

| Layer    | Technology                                   |
| -------- | -------------------------------------------- |
| Language | Python (Jupyter notebook)                    |
| LLM      | `qwen2:7b` via Ollama (OpenAI-compatible API) |
| Client   | `openai` Python SDK                          |

More about it: [Dummy Agent Library](unit-1-introduction-to-agents/project-1-dummy-agent-library/README.md)

#### Project 2: Agent using smolagents — [`project-2-agent-using-smolagents/`](unit-1-introduction-to-agents/project-2-agent-using-smolagents)

**Status:** Not started

More about the unit: [Unit 1](unit-1-introduction-to-agents/README.md)
