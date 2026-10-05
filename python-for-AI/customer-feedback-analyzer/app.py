from collections import Counter
from pathlib import Path
from typing import Any

import streamlit as st

from api import AnalysisResponse, ReviewRequest, analyze_feedback
from db import init_db, load_history, save_result


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


def response_to_dict(
    review: str, response: AnalysisResponse
) -> dict[str, Any]:
    return {
        "review": review,
        "label": response.label,
        "score": response.score,
        "theme": response.theme,
    }


def analyze_reviews(reviews: list[str]) -> list[dict[str, Any]]:
    """Analyze each review and return database-compatible result dictionaries."""
    results: list[dict[str, Any]] = []
    progress = st.progress(0)
    status = st.empty()

    for index, review in enumerate(reviews, start=1):
        status.write(f"Analyzing review {index} of {len(reviews)}...")
        try:
            response = analyze_review(review)
        except Exception as exc:
            status.error(f"Review {index} could not be analyzed: {exc}")
            continue
        results.append(response_to_dict(review, response))
        progress.progress(index / len(reviews))

    status.empty()
    progress.empty()
    return results


def set_review_from_sample() -> None:
    """Copy selected samples into the editable review field."""
    selected_reviews = st.session_state.sample_reviews
    st.session_state.review_text = "\n".join(selected_reviews)


def show_results(results: list[dict[str, Any]]) -> None:
    """Render the current analysis and database actions."""
    st.subheader("Results")

    if len(results) == 1:
        st.table(
            [
                {
                    "Review": results[0]["review"],
                    "Sentiment": results[0]["label"].title(),
                    "Score": f'{results[0]["score"]}/5',
                    "Theme": results[0]["theme"].title(),
                }
            ]
        )
    else:
        average_score = sum(result["score"] for result in results) / len(results)
        positive_count = sum(result["label"].lower() == "positive" for result in results)
        positive_percentage = positive_count / len(results) * 100
        theme_counts = Counter(result["theme"] for result in results)
        most_analyzed_theme, _ = theme_counts.most_common(1)[0]

        summary_columns = st.columns(3)
        summary_columns[0].metric("Reviews analyzed", len(results))
        summary_columns[1].metric("Average score", f"{average_score:.1f}/5")
        summary_columns[2].metric("Positive", f"{positive_percentage:.0f}%")

        st.dataframe(
            [
                {
                    "Review": result["review"],
                    "Sentiment": result["label"].title(),
                    "Score": f'{result["score"]}/5',
                    "Theme": result["theme"].title(),
                }
                for result in results
            ],
            use_container_width=True,
            hide_index=True,
        )
        st.write(f"**Most analyzed theme:** {most_analyzed_theme.title()}")

    if st.button("Save result to database", type="secondary"):
        try:
            save_result(results)
        except Exception as exc:
            st.error(f"Unable to save results: {exc}")
        else:
            st.success(f"Saved {len(results)} result(s) to the database.")


st.set_page_config(
    page_title="Customer Feedback Analyzer",
    page_icon="🍽️",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container { max-width: 1100px; padding-top: 3rem; }
    h1 { letter-spacing: -0.04em; }
    .stButton > button { border-radius: 0.6rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

init_db()
sample_reviews = load_sample_reviews()

if "review_text" not in st.session_state:
    st.session_state.review_text = ""
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = []

st.title("🍽️ Customer Feedback Analyzer")
st.caption("Understand the sentiment, score, and main theme of every review.")

st.subheader("Restaurant review")
sample_columns = st.columns([4, 1])
with sample_columns[0]:
    st.multiselect(
        "Choose sample reviews",
        options=sample_reviews,
        key="sample_reviews",
        on_change=set_review_from_sample,
        placeholder="Choose one or more sample reviews",
        label_visibility="collapsed",
    )
with sample_columns[1]:
    analyze_all = st.button(
        "Analyze all samples",
        help="Analyze every review in sample_reviews.txt",
        type="tertiary",
    )

st.text_area(
    "Review text",
    key="review_text",
    height=180,
    placeholder="Enter one review per line to analyze multiple reviews...",
    label_visibility="collapsed",
)

if st.button("Analyze", type="primary"):
    reviews = [line.strip() for line in st.session_state.review_text.splitlines() if line.strip()]
    if not reviews:
        st.warning("Enter at least one review before analyzing.")
    else:
        with st.spinner("Analyzing reviews..."):
            st.session_state.analysis_results = analyze_reviews(reviews)

if analyze_all:
    if sample_reviews:
        with st.spinner("Analyzing sample reviews..."):
            st.session_state.analysis_results = analyze_reviews(sample_reviews)
    else:
        st.info("No sample reviews were found in sample_reviews.txt.")

if st.session_state.analysis_results:
    show_results(st.session_state.analysis_results)

st.divider()
st.subheader("History")
if st.button("Load history", type="secondary"):
    try:
        history = load_history()
    except Exception as exc:
        st.error(f"Unable to load history: {exc}")
    else:
        if history:
            st.dataframe(history, use_container_width=True, hide_index=True)
        else:
            st.info("No saved results yet.")
