"""SQLite3 Database connection"""
import sqlite3
from pathlib import Path
from typing import Iterator, Optional

#
DB_FILE = Path(__file__).resolve().parent / "dealership.db"

def connect(db_path: Optional[str] = None) -> sqlite3.Connection:
    """"""
    path = Path(db_path) if db_path else DB_FILE
    conn = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn

def row_to_dicts(rows: Iterator[sqlite3.Row]) -> list[dict]:
    """"""
    return [dict(row) for row in rows]
