# learn-AI

A personal learning repository where I track and store the files from the projects I build while learning AI.

I'm following a self-made 2–3 month path that starts from Python revision for AI and goes all the way to building AI agents, MCP (Model Context Protocol) and RAG (Retrieval-Augmented Generation). The path is made up of around 5 courses, and each course ends with (or includes) hands-on projects that live in this repo.

## Repository Structure

Each top-level folder is a **course**, and each subfolder inside it is a **project** from that course.

```
learn-AI/
├── README.md
├── 1-python-for-AI/                # Course 1: Python for AI (YouTube: Codebasics)
│   └── customer-feedback-analyzer/ # Project: Customer Feedback Analyzer
├── 2-anthropic-mcp-course/         # Course 2: Introduction to Model Context Protocol (Anthropic)
│   └── cli-based-chatbot/          # Project: MCP Chat (CLI-based chatbot)
└── 3-ai-agents-course/             # Course 3: AI Agents Course (Hugging Face)
    └── unit-1-introduction-to-agents/
        ├── project-1-dummy-agent-library/     # Project: Dummy Agent Library
        └── project-2-agent-using-smolagents/  # Project: Agent using smolagents (not started)
```

> The tree will grow as I move through the learning path and add new courses and projects.

## Courses & Projects

### 1. Python for AI — [`1-python-for-AI/`](1-python-for-AI)

**Course:** [Python for AI (YouTube)](https://www.youtube.com/watch?v=6GuyMZ-cSzE)

The first course of the path. It revises Python with a focus on what is needed for AI work, and finishes with a small end-to-end project that puts it into practice by calling an LLM API from a real app.

**Status:** Completed

#### Project: Customer Feedback Analyzer — [`1-python-for-AI/customer-feedback-analyzer/`](1-python-for-AI/customer-feedback-analyzer)

A tool that analyzes a business's Google reviews and performs sentiment analysis on them.

**How it works**

1. The user pastes reviews into a text field, one review per line, and clicks **Analyze**.
2. The frontend calls the backend, which uses the Gemini API to perform sentiment analysis.
3. For each review, the result shows:
   - **Label:** positive or negative
   - **Score:** out of 5
   - **Theme:** the main topic of the review
4. A **summary** is shown for all reviews: the average score and the percentage of positive reviews.
5. A **Save report** button stores the report in the database.

**Tech stack**

| Layer    | Technology |
| -------- | ---------- |
| Frontend | Streamlit  |
| Backend  | FastAPI    |
| Database | SQLite     |
| LLM      | Gemini API |

More about it: [Customer Feedback Analyzer](1-python-for-AI/customer-feedback-analyzer/README.md)

---

### 2. Introduction to Model Context Protocol — [`2-anthropic-mcp-course/`](2-anthropic-mcp-course)

**Course:** [Introduction to Model Context Protocol (Anthropic)](https://anthropic.skilljar.com/introduction-to-model-context-protocol)

**Certificate:** [Verify my certificate](https://verify.skilljar.com/c/exgc7tihdpee)

The second course of the path, by Anthropic. It covers the Model Context Protocol (MCP): how to build MCP servers that expose tools, resources and prompts, how to build an MCP client that connects to them, and how to wire both into a chatbot that uses the Anthropic API. The course is built around one hands-on project.

**Status:** Completed

#### Project: MCP Chat (CLI-based chatbot) — [`2-anthropic-mcp-course/cli-based-chatbot/`](2-anthropic-mcp-course/cli-based-chatbot)

A command-line chatbot that talks to Claude through the Anthropic API and uses MCP to give it access to a small set of documents.

**What it does**

- **MCP server** (`mcp_server.py`) holds a set of in-memory documents and exposes:
  - **Tools:** read a document and edit a document (find and replace)
  - **Resources:** list all document IDs and fetch a single document's contents
  - **Prompts:** `format_document` (rewrite a document in markdown) and `summarize_doc`
- **MCP client** (`mcp_client.py`) connects to the server and calls its tools, resources and prompts.
- **CLI chat** lets you:
  - chat with the model by typing a message
  - include a document in your query with `@`, e.g. `Tell me about @deposition.md`
  - run server prompts as commands with `/`, e.g. `/summarize_doc deposition.md`, with Tab auto-complete
- The server can be tested on its own with the **MCP Inspector** (`mcp dev mcp_server.py`).

**Tech stack**

| Layer        | Technology                       |
| ------------ | -------------------------------- |
| Language     | Python                           |
| Protocol     | MCP (`mcp[cli]`, FastMCP server) |
| LLM          | Claude via the Anthropic API     |
| CLI          | prompt-toolkit                   |
| Package mgmt | uv                               |

More about it: [MCP Chat](2-anthropic-mcp-course/cli-based-chatbot/README.md)

---

### 3. AI Agents Course — [`3-ai-agents-course/`](3-ai-agents-course)

**Course:** [AI Agents Course (Hugging Face)](https://huggingface.co/learn/agents-course/unit0/introduction)

The third course of the path. A free, self-paced course from Hugging Face that goes from agent fundamentals (tools, thoughts, actions, observations) to building agents with the smolagents, LangGraph and LlamaIndex frameworks, then real-world use cases and a benchmark-based final challenge. It also has bonus units on fine-tuning for function-calling, agent observability and evaluation, and Pokémon battle agents.

**Status:** In progress

The course is organized by **unit**, and each unit contains its own projects. Projects will be added here as I complete them.

#### Unit 1: Introduction to Agents — [`3-ai-agents-course/unit-1-introduction-to-agents/`](3-ai-agents-course/unit-1-introduction-to-agents)

**Status:** In progress

##### Project: Dummy Agent Library — [`project-1-dummy-agent-library/`](3-ai-agents-course/unit-1-introduction-to-agents/project-1-dummy-agent-library)

A notebook that builds an agent from scratch, without any framework, to show what happens under the hood.

**How it works**

1. A ReAct-style system prompt describes a dummy `get_weather` tool and forces the Thought / Action / Observation format.
2. Generation is stopped at `Observation:` so the model can't hallucinate the tool result.
3. The notebook runs the tool with the arguments the model chose and appends the result as an Observation.
4. The model then produces the final answer.

**Tech stack**

| Layer    | Technology                                    |
| -------- | --------------------------------------------- |
| Language | Python (Jupyter notebook)                     |
| LLM      | `qwen2:7b` via Ollama (OpenAI-compatible API) |
| Client   | `openai` Python SDK                           |

More about it: [Dummy Agent Library](3-ai-agents-course/unit-1-introduction-to-agents/project-1-dummy-agent-library/README.md)

> Next up in this unit: an agent built with the `smolagents` library.

More about the course: [AI Agents Course](3-ai-agents-course/README.md)
