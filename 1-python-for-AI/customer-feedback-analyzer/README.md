# Customer Feedback Analyzer

Customer Feedback Analyzer is a small AI-powered restaurant review application.
It accepts one or more customer reviews, sends each review to Google's Gemini
API, and presents a structured analysis:

- **Sentiment:** positive, negative, or neutral
- **Score:** a rating from 1 (very bad) to 5 (very good)
- **Theme:** the primary topic, such as service, quality, price, or delivery

The project includes a Streamlit interface for interactive use and a FastAPI
endpoint for programmatic access. Analysis results can be saved to a local
SQLite database and loaded later as history.

## Features

- Analyze a single review or multiple reviews, one review per line.
- Select one or more bundled sample reviews from the multi-select menu.
- Analyze all bundled sample reviews at once.
- Display an individual result in a readable table.
- Display batch summaries with:
  - Number of reviews analyzed
  - Average score
  - Percentage of positive reviews
  - Most frequently analyzed theme
- Save analyzed results to SQLite.
- Load previously saved results from the database.
- Expose the same analysis functionality through `POST /analyze-feedback`.

## Technology stack

| Area | Technology |
| --- | --- |
| User interface | Streamlit |
| API | FastAPI |
| Data validation | Pydantic |
| AI model | Google Gemini API |
| Database | SQLite |
| Dependency management | uv |
| Language | Python 3.13 or newer |

## Project files

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit interface and application workflow |
| `api.py` | FastAPI application and Gemini-powered analysis endpoint |
| `db.py` | SQLite initialization, saving, and history loading |
| `sample_reviews.txt` | Bundled one-review-per-line sample data |
| `pyproject.toml` | Project metadata and dependencies |
| `uv.lock` | Reproducible dependency lockfile |
| `feedback.db` | Runtime database created automatically; not committed |

## Prerequisites

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) installed
- A free Gemini API key

### Create a free Gemini API key

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with a Google account.
3. Create or retrieve an API key.
4. Keep the key private and do not commit it to source control.

## Setup

From this project directory:

```powershell
uv sync
```

Create a `.env` file in the same directory as `api.py` and add your Gemini
key:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

The repository ignores `.env` files by default. Never replace the placeholder
with a real key in a committed file.

## Run the Streamlit application

```powershell
uv run streamlit run app.py
```

Streamlit will print a local URL, usually
`http://localhost:8501`, which you can open in a browser.

The SQLite database is initialized automatically when the application starts.
It is created in the current working directory as `feedback.db` and is ignored
by Git so every user can create their own local history.

## Run the FastAPI API

```powershell
uv run uvicorn api:app --reload
```

The API is then available at `http://localhost:8000`.
Interactive API documentation is available at
`http://localhost:8000/docs`.

### Analyze a review through the API

Send a `POST` request to `/analyze-feedback` with JSON containing a `text`
field:

```json
{
  "text": "The food was delicious and the staff were very friendly."
}
```

Example PowerShell request:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:8000/analyze-feedback `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"text":"The food was delicious and the staff were very friendly."}'
```

The response contains `label`, `score`, and `theme` fields.

## Database behavior

The application uses SQLite through the functions in `db.py`:

- `init_db()` creates the `feedback` table if it does not exist.
- `save_result()` stores one or more analysis results.
- `load_history()` returns all saved results.

`feedback.db` is local application data and is intentionally ignored. Delete
it if you want to start with an empty history.

## Development notes

Run commands from the project directory so the local `.env` file and
`feedback.db` are discovered consistently. The FastAPI endpoint and Streamlit
interface share the same analysis models and handler in `api.py`.
