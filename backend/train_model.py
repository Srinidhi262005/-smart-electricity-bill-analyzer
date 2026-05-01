from models.ml_model import train_model, save_model


if __name__ == '__main__':
    model, metrics = train_model(model_type='random_forest')
    save_model(model)
    print('Trained model saved successfully.')
    print('Metrics:', metrics)
