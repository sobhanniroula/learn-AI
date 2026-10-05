from collections import Counter
from pathlib import Path
from typing import Any

import streamlit as st

from api import AnalysisResponse, ReviewRequest, analyze_feedback


PROJECT_ROOT = Path(__file__).parent
SAMPLE_REVIEWS_PATH = PROJECT_ROOT / "sample_reviews.txt"


def load_sample_reviews() -> list[str]:
    """Load non-empty sample reviews bundled with the project."""
    if not SAMPLE_REVIEWS_PATH.exists():
        return []
    return [
        line.strip()
        for line in SAMPLE_REVIEWS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def analyze_review(text: str) -> AnalysisResponse:
    """Run the same handler used by POST /analyze-feedback."""
    return analyze_feedback(ReviewRequest(text=text))


def response_to_dict(response: AnalysisResponse) -> dict[str, Any]:
    return {
        "label": response.label,
        "score": response.score,
        "theme": response.theme,
    }


st.set_page_config(
    page_title="Customer Feedback Analyzer",
    page_icon="🍽️",
    layout="wide",
)

st.title("🍽️ Customer Feedback Analyzer")
st.write("Analyze restaurant reviews using the existing `/analyze-feedback` API.")

with st.sidebar:
    st.header("API")
    st.code("POST /analyze-feedback")
    st.caption(
        "The Streamlit interface calls the same request model and handler as the "
        "FastAPI endpoint."
    )

    sample_reviews = load_sample_reviews()
    selected_review = st.selectbox(
        "Load a sample review",
        options=["Choose a sample"] + sample_reviews,
    )

review_text = st.text_area(
    "Restaurant review",
    value="" if selected_review == "Choose a sample" else selected_review,
    height=180,
    placeholder="Enter a restaurant review to analyze...",
)

if st.button("Analyze review", type="primary"):
    if not review_text.strip():
        st.warning("Enter a review before analyzing it.")
    else:
        with st.spinner("Analyzing review..."):
            try:
                result = analyze_review(review_text.strip())
            except Exception as exc:
                st.error(f"Unable to analyze the review: {exc}")
            else:
                columns = st.columns(3)
                columns[0].metric("Sentiment", result.label.title())
                columns[1].metric("Score", f"{result.score}/5")
                columns[2].metric("Theme", result.theme.title())
                st.json(response_to_dict(result))

st.divider()
st.subheader("Analyze sample reviews")

if sample_reviews and st.button("Analyze all sample reviews"):
    results: list[dict[str, Any]] = []
    sentiment_counts: Counter[str] = Counter()
    progress = st.progress(0)
    status = st.empty()

    for index, review in enumerate(sample_reviews, start=1):
        status.write(f"Analyzing review {index} of {len(sample_reviews)}...")
        try:
            result = analyze_review(review)
        except Exception as exc:
            status.error(f"Review {index} failed: {exc}")
            continue
        results.append({"review": review, **response_to_dict(result)})
        sentiment_counts[result.label] += 1
        progress.progress(index / len(sample_reviews))

    status.empty()
    if results:
        st.dataframe(results, use_container_width=True, hide_index=True)
        st.bar_chart(sentiment_counts)
elif not sample_reviews:
    st.info("No sample reviews were found in sample_reviews.txt.")