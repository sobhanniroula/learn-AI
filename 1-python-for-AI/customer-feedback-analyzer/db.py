"""
All the database related functions are defined in this file.

Keeping this db code in its own file makes app.py shorter and easier to read.
app.py just calls the functions defined here, and doesn't need to know how they work.
"""

import sqlite3

# Our db file. It stores every review we ever analyze.
DB_FILE = "feedback.db"

def init_db():
    """Create the feedback table the first time we run the application."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review TEXT NOT NULL,
            label TEXT NOT NULL,
            score INTEGER NOT NULL,
            theme TEXT
        )
        """
    )
    conn.commit()
    conn.close()

def save_result(results):
    """Save all analyzed reviews to the database."""
    conn = sqlite3.connect(DB_FILE)
    for r in results:
        conn.execute(
            "INSERT INTO feedback (review, label, score, theme) VALUES (?, ?, ?, ?)",
            (r["review"], r["label"], r["score"], r["theme"]),
        )
    conn.commit()
    conn.close()

def load_history():
    """Load all analyzed reviews we have saved so far from the database."""
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute("SELECT review, label, score, theme FROM feedback")
    results = [
        {"review": row[0], "label": row[1], "score": row[2], "theme": row[3]}
        for row in rows.fetchall()
    ]
    conn.close()
    return results