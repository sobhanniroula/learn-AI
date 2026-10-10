# Dummy Agent Library

> Project from Unit 1 of the [AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) by Hugging Face (course 3 in my [learn-AI](../../../README.md) repo).

A Jupyter notebook that builds a minimal agent from scratch, without any agent framework, to show what an agent really is under the hood: an LLM, a system prompt that describes the tools, a loop of **Thought → Action → Observation**, and some code that actually runs the tool.

The agent has a single dummy tool, `get_weather`, which always returns a fixed answer. The point is the mechanics, not the tool.

## Project Structure

| File | Purpose |
| ---- | ------- |
| `dummy-agent-library.ipynb` | The whole project: client setup, system prompt, the dummy tool and the agent steps |
| `.env` | Holds `HF_TOKEN` (not committed with real values) |

## What the notebook does

1. **Connects to an LLM.** The course uses the Hugging Face Serverless API (`InferenceClient`), but that needs a paid plan for the token, so I use a local model served by [Ollama](https://ollama.com) (`qwen2:7b`) through its OpenAI-compatible endpoint (`http://localhost:11434/v1`). The original `InferenceClient` lines are kept as comments.
2. **Sends a plain chat request** (`"The capital of Finland is"` → `Helsinki.`) to check that the model responds.
3. **Defines a ReAct-style system prompt** that lists the available tool (`get_weather`) and forces the model to answer in the `Thought` / `Action` (JSON blob) / `Observation` format.
4. **Shows the hallucination problem.** Without a stop sequence the model invents the `Observation` and the final answer itself.
5. **Stops generation at `Observation:`** with `stop=["Observation:"]`, so the model only produces the Thought and the Action JSON (`{"action": "get_weather", "action_input": {"location": "London"}}`).
6. **Runs the tool.** A dummy `get_weather(location)` function returns a fixed string.
7. **Feeds the result back** as an `Observation` appended to the conversation, and the model produces the `Final Answer`.

### The agent cycle

```
Question → Thought → Action (JSON) → [generation stops] → run tool → Observation → Thought → Final Answer
```

## Key takeaways

- An agent is an LLM plus tools plus a loop; the "tool calling" is just text the model writes in an agreed format.
- The model must be **stopped** before the `Observation`, otherwise it hallucinates the tool result.
- The code around the model (parsing the action, calling the function, appending the observation) is what makes it an agent.
- Small local models follow the format only roughly (e.g. the first Action JSON came back with doubled braces and a wrongly nested `location`), so prompts and parsing need to be forgiving.

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com) running locally with the `qwen2:7b` model pulled (`ollama pull qwen2:7b`)
- Jupyter (VS Code notebooks or JupyterLab)

## Setup

1. Install the dependencies:

```bash
pip install openai python-dotenv huggingface_hub
```

2. Create a `.env` file in this folder (only needed if you switch back to the Hugging Face `InferenceClient`):

```
HF_TOKEN=""  # Hugging Face access token
```

3. Start Ollama and make sure the model is available:

```bash
ollama pull qwen2:7b
ollama serve
```

4. Open `dummy-agent-library.ipynb` and run the cells from top to bottom.

## Notes

- To use a different model, change the `model=` argument in the `client.chat.completions.create(...)` calls.
- The `extra_body={'thinking': {'type': 'disabled'}}` argument is a leftover from the hosted model setup; Ollama simply ignores it.
