# MCP Chat

> Project from the [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) course by Anthropic (course 2 in my [learn-AI](../../README.md) repo).

MCP Chat is a command-line interface application that enables interactive chat capabilities with AI models through the Anthropic API. The application supports document retrieval, command-based prompts, and extensible tool integrations via the MCP (Model Context Protocol) architecture.

## Project Structure

| File | Purpose |
| ---- | ------- |
| `main.py` | Entry point; loads `.env`, starts the MCP client(s) and the CLI |
| `mcp_server.py` | MCP server with the document tools, resources and prompts |
| `mcp_client.py` | MCP client used to connect to the server |
| `core/` | Claude service, chat loop, tool handling and CLI |

## Prerequisites

- Python 3.9+
- Anthropic API Key (from [console.anthropic.com](https://console.anthropic.com); a Claude subscription does not include API access)

## Setup

### Step 1: Configure the environment variables

1. Create or edit the `.env` file in the project root and verify that the following variables are set correctly:

```
ANTHROPIC_API_KEY=""  # Enter your Anthropic API secret key
CLAUDE_MODEL=""       # A current model ID, e.g. claude-haiku-4-5-20251001
```

### Step 2: Install dependencies

#### Option 1: Setup with uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

1. Install uv, if not already installed:

```bash
pip install uv
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
uv pip install -e .
```

4. Run the project

```bash
uv run main.py
```

#### Option 2: Setup without uv

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install anthropic python-dotenv prompt-toolkit "mcp[cli]==1.8.0"
```

3. Run the project

```bash
python main.py
```

## Usage

### Basic Interaction

Simply type your message and press Enter to chat with the model.

### Document Retrieval

Use the @ symbol followed by a document ID to include document content in your query:

```
> Tell me about @deposition.md
```

### Commands

Use the / prefix to execute commands defined in the MCP server:

```
> /summarize_doc deposition.md
```

Commands will auto-complete when you press Tab.

## MCP Server Features

| Type     | Name                  | Description |
| -------- | --------------------- | ----------- |
| Tool     | `read_doc_contents`   | Read the contents of a document |
| Tool     | `edit_doc_contents`   | Replace a string in a document with another string |
| Resource | `docs://documents`    | List all document IDs |
| Resource | `docs://documents/{doc_id}` | Get the contents of one document |
| Prompt   | `format_document`     | Rewrite a document in markdown format |
| Prompt   | `summarize_doc`       | Summarize a document |

### Testing with the MCP Inspector

```bash
uv run mcp dev mcp_server.py
```

If the Inspector doesn't prefill the connection, set Transport to STDIO, Command to `uv` and Arguments to `run mcp_server.py`.

## Development

### Adding New Documents

Edit the `mcp_server.py` file to add new documents to the `docs` dictionary.

### Linting and Typing Check

There are no lint or type checks implemented.
