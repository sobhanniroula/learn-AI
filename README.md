# learn-AI

A personal learning repository where I track and store the files from the projects I build while learning AI.

I'm following a self-made 2–3 month path that starts from Python revision for AI and goes all the way to building AI agents, MCP (Model Context Protocol) and RAG (Retrieval-Augmented Generation). The path is made up of around 5 courses, and each course ends with (or includes) hands-on projects that live in this repo.

## Repository Structure

Each top-level folder is a **course**, and each subfolder inside it is a **project** from that course.

```
learn-AI/
├── README.md
└── python-for-AI/                  # Course 1: Python for AI
    └── customer-feedback-analyzer/ # Project: Customer Feedback Analyzer
```

> The tree will grow as I move through the learning path and add new courses and projects.

## Courses & Projects

### 1. Python for AI — [`python-for-AI/`](python-for-AI)

**Course:** [Python for AI (YouTube)](https://www.youtube.com/watch?v=6GuyMZ-cSzE)

The first course of the path. It revises Python with a focus on what is needed for AI work, and finishes with a small end-to-end project that puts it into practice by calling an LLM API from a real app.

**Status:** In progress

#### Project: Customer Feedback Analyzer — [`python-for-AI/customer-feedback-analyzer/`](python-for-AI/customer-feedback-analyzer)

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

More about it: [Customer Feedback Analyzer](python-for-AI/customer-feedback-analyzer/README.md)
