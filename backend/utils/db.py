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
            # Raw initialization logic removed; schema managed by models.py
            conn.commit()
            logger.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")


def get_db_connection(db_path):
    """Establishes and returns a SQLite connection with Row factory."""
    try:
        if not os.path.exists(db_path):
            init_db(db_path)
            
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        logger.error(f"Failed to connect to database: {e}")
        return None
