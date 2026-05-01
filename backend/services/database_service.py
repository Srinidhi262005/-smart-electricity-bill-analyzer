from sqlalchemy.orm import sessionmaker
from models.user import User
from models.usage_history import UsageHistory
from models.insights_log import InsightsLog
from utils.sqlalchemy_db import get_engine

engine = get_engine()
Session = sessionmaker(bind=engine)

def create_user(name, email, password):
    """Create a new user."""
    session = Session()
    try:
        user = User(name=name, email=email, password=password)
        session.add(user)
        session.commit()
        return user.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_user_by_email(email):
    """Get user by email."""
    session = Session()
    try:
        return session.query(User).filter_by(email=email).first()
    finally:
        session.close()

def save_usage_history(user_id, units, predicted_bill):
    """Save usage history for a user."""
    session = Session()
    try:
        history = UsageHistory(user_id=user_id, units=units, predicted_bill=predicted_bill)
        session.add(history)
        session.commit()
        return history.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def save_insight_log(user_id, suggestion):
    """Save insight/suggestion for a user."""
    session = Session()
    try:
        log = InsightsLog(user_id=user_id, suggestion=suggestion)
        session.add(log)
        session.commit()
        return log.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_user_history(user_id, limit=10):
    """Get usage history for a user."""
    session = Session()
    try:
        return session.query(UsageHistory).filter_by(user_id=user_id).order_by(UsageHistory.date.desc()).limit(limit).all()
    finally:
        session.close()