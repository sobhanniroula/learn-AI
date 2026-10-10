# Unit 1: Introduction to Agents

Unit 1 of the [AI Agents Course](../README.md) by Hugging Face (course 3 in my [learn-AI](../../README.md) repo).

**Status:** In progress

## About the unit

The foundations of agents: what an agent is, how an LLM is used as its "brain", how tools extend what it can do, and the **Thought → Action → Observation** cycle that ties it together. It also gives a refresher on LLMs, messages and special tokens, and ends with building a first agent with the `smolagents` library.

Finishing this unit earns the course's **Fundamentals Certificate**.

## Topics

- What an agent is and where it is useful
- LLMs, messages, special tokens and chat templates
- Tools and how an agent calls them
- The agent workflow: Thought, Action, Observation
- Thought/Action/Observation with the ReAct approach (`Reason` + `Act`)
- Code agents vs. JSON agents

## Projects

| # | Project | What it is | Status |
| - | ------- | ---------- | ------ |
| 1 | [Dummy Agent Library](project-1-dummy-agent-library/README.md) | A minimal agent built from scratch in a notebook: ReAct system prompt, stop sequence, a dummy `get_weather` tool and the Observation fed back to the LLM | Completed |
| 2 | [Agent using smolagents](project-2-agent-using-smolagents/README.md) | The same idea built with the `smolagents` library | Not started |

### Project 1: Dummy Agent Library

Builds an agent without any framework, using a local `qwen2:7b` model through Ollama. It shows why generation has to be stopped at `Observation:` (otherwise the model hallucinates the tool result), how the dummy `get_weather` function is executed, and how its output is appended to the conversation so the model can give a final answer.

More about it: [Dummy Agent Library](project-1-dummy-agent-library/README.md)

### Project 2: Agent using smolagents

To be done after the Unit 1 smolagents section.
