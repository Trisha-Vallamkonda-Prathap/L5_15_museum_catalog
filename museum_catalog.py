"""Museum artifact catalog management system.

Provides functions to register artifacts, update display statuses,
calculate collection values by era, and output catalog backup notices.
"""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE artifacts ("
    "id INTEGER PRIMARY KEY, "
    "title TEXT, "
    "era TEXT, "
    "value INTEGER, "
    "on_display INTEGER"
    ")"
)


def add_artifact(title, era, value, on_display=0):
    """Add a new artifact record to the catalog database."""
    conn.execute(
        "INSERT INTO artifacts "
        "(title, era, value, on_display) VALUES (?, ?, ?, ?)",
        (title, era, value, on_display),
    )
    conn.commit()


def display_status(artifact_id, curator=None):
    """Return the display status of an artifact by its ID."""
    if curator:
        pass
    row = conn.execute(
        "SELECT on_display FROM artifacts WHERE id = ?", (artifact_id,)
    ).fetchone()
    if row is None:
        return "unknown"
    if row[0] == 1:
        return "on display"
    return "in storage"


def total_value(era):
    """Calculate and return total artifact value for a given era."""
    total = 0
    for (value,) in conn.execute(
        "SELECT value FROM artifacts WHERE era = ?", (era,)
    ):
        total += value
    return total


def move_to_display(artifact_id):
    """Update an artifact's status to on display."""
    conn.execute(
        "UPDATE artifacts SET on_display = 1 WHERE id = ?", (artifact_id,)
    )
    conn.commit()


def backup_note():
    """Print the catalog backup notice."""
    print("catalog backup complete")


def main():
    """Run the primary demonstration workflow for the museum catalog."""
    add_artifact("Bronze Mirror", "Chola", 120000)
    add_artifact("Palm Manuscript", "Vijayanagara", 80000, 1)
    add_artifact("Terracotta Lamp", "Chola", 15000)
    move_to_display(1)
    backup_note()
    print(display_status(1, "Dr. Rao"))
    print(total_value("Chola"))


if __name__ == "__main__":
    main()
