from datetime import datetime
from sqlalchemy.exc import IntegrityError
from utils.sqlalchemy_db import get_session_factory
from models.user import User
from models.usage_history import UsageHistory
from models.insights_log import InsightsLog

Session = get_session_factory()


def create_user(name, email, password):
    """Create a new user record."""
    session = Session()
    user = User(name=name, email=email, password=password)
    session.add(user)
    try:
        session.commit()
        session.refresh(user)
        return user
    except IntegrityError:
        session.rollback()
        return None
    finally:
        session.close()


def get_user_by_id(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user


def get_user_by_email(email):
    session = Session()
    user = session.query(User).filter(User.email == email).first()
    session.close()
    return user


def update_user(user_id, **updates):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        session.close()
        return None
    for key, value in updates.items():
        if hasattr(user, key):
            setattr(user, key, value)
    session.commit()
    session.refresh(user)
    session.close()
    return user


def delete_user(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        session.close()
        return False
    session.delete(user)
    session.commit()
    session.close()
    return True


def add_usage_history(user_id, units, predicted_bill, date=None):
    session = Session()
    if date is None:
        date = datetime.utcnow()
    record = UsageHistory(user_id=user_id, units=units, predicted_bill=predicted_bill, date=date)
    session.add(record)
    session.commit()
    session.refresh(record)
    session.close()
    return record


def get_usage_history_for_user(user_id):
    session = Session()
    records = session.query(UsageHistory).filter(UsageHistory.user_id == user_id).order_by(UsageHistory.date.desc()).all()
    session.close()
    return records


def update_usage_history(record_id, **updates):
    session = Session()
    record = session.query(UsageHistory).filter(UsageHistory.id == record_id).first()
    if record is None:
        session.close()
        return None
    for key, value in updates.items():
        if hasattr(record, key):
            setattr(record, key, value)
    session.commit()
    session.refresh(record)
    session.close()
    return record


def delete_usage_history(record_id):
    session = Session()
    record = session.query(UsageHistory).filter(UsageHistory.id == record_id).first()
    if record is None:
        session.close()
        return False
    session.delete(record)
    session.commit()
    session.close()
    return True


def add_insight_log(user_id, suggestion, date=None):
    session = Session()
    if date is None:
        date = datetime.utcnow()
    insight = InsightsLog(user_id=user_id, suggestion=suggestion, date=date)
    session.add(insight)
    session.commit()
    session.refresh(insight)
    session.close()
    return insight


def get_insights_for_user(user_id):
    session = Session()
    records = session.query(InsightsLog).filter(InsightsLog.user_id == user_id).order_by(InsightsLog.date.desc()).all()
    session.close()
    return records


def delete_insight_log(insight_id):
    session = Session()
    insight = session.query(InsightsLog).filter(InsightsLog.id == insight_id).first()
    if insight is None:
        session.close()
        return False
    session.delete(insight)
    session.commit()
    session.close()
    return True
