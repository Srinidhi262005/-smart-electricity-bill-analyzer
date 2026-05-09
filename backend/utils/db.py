import os
import sqlite3
import logging

logger = logging.getLogger(__name__)


def init_db(db_path):
    """Initializes the database schema with error handling and context managers."""
    try:
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS bill_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    units REAL NOT NULL,
                    predicted_amount REAL NOT NULL,
                    actual_amount REAL,
                    anomaly_flag INTEGER DEFAULT 0,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                );
                '''
            )
            conn.commit()
            logger.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")


def get_db_connection(db_path):
    """Establishes and returns a database connection."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logger.error(f"Failed to connect to database: {e}")
        return None
