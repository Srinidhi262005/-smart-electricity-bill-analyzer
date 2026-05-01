import os
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from utils.config import Config

MODEL_PATH = Config.MODEL_PATH
TRAINING_DATA_PATH = Config.TRAINING_DATA_PATH


def create_dummy_dataset(num_samples=200):
    """Generate a synthetic dataset of units vs bill amount."""
    np.random.seed(42)
    units = np.linspace(0, 650, num_samples)

    def slab_cost(x):
        if x <= 100:
            return x * 4.5
        if x <= 200:
            return 100 * 4.5 + (x - 100) * 6.5
        if x <= 400:
            return 100 * 4.5 + 100 * 6.5 + (x - 200) * 8.5
        return 100 * 4.5 + 100 * 6.5 + 200 * 8.5 + (x - 400) * 9.5

    amounts = np.array([slab_cost(u) for u in units])
    noise = np.random.normal(0, 8, len(units))
    bill_amount = np.clip(amounts * 1.02 + noise, 0, None)

    dataset = pd.DataFrame({'units': units, 'bill_amount': bill_amount})
    os.makedirs(os.path.dirname(TRAINING_DATA_PATH), exist_ok=True)
    dataset.to_csv(TRAINING_DATA_PATH, index=False)
    return dataset


def train_model(model_type='random_forest', test_size=0.2, random_state=42):
    """Train a regression model on the dummy electricity bill dataset."""
    data = create_dummy_dataset()
    X = data[['units']].values
    y = data['bill_amount'].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    if model_type == 'linear':
        model = LinearRegression()
    else:
        model = RandomForestRegressor(
            n_estimators=100,
            max_depth=8,
            n_jobs=-1,
            random_state=random_state,
        )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    metrics = {
        'mae': round(mean_absolute_error(y_test, predictions), 2),
        'r2': round(r2_score(y_test, predictions), 4),
        'model_type': model_type,
        'test_samples': len(y_test),
    }

    return model, metrics


def save_model(model, path=MODEL_PATH):
    """Persist the trained ML model to disk."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as model_file:
        pickle.dump(model, model_file)


def load_model(path=MODEL_PATH):
    """Load an existing model from disk, training one if needed."""
    if not os.path.exists(path):
        model, _ = train_model()
        save_model(model, path)
        return model

    with open(path, 'rb') as model_file:
        return pickle.load(model_file)


def predict_bill(units, model=None):
    """Predict bill amount for a given unit consumption."""
    if model is None:
        model = load_model()

    units_value = float(units)
    prediction = model.predict(np.array([[units_value]]))[0]
    return round(float(max(prediction, 0)), 2)


if __name__ == '__main__':
    trained_model, metrics = train_model(model_type='random_forest')
    save_model(trained_model)
    print('Model trained and saved at:', MODEL_PATH)
    print('Training metrics:', metrics)
