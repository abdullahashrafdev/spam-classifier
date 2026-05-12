import pytest
from app import app

# This creates a test version of your app
@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

# Test that the API returns a prediction
def test_predict_spam(client):
    response = client.post("/predict", json={"text": "Win a free iPhone now!"})
    assert response.status_code == 200
    assert "prediction" in response.get_json()

# Test that the prediction is either spam or ham
def test_prediction_value(client):
    response = client.post("/predict", json={"text": "Hey how are you?"})
    result = response.get_json()
    assert result["prediction"] in ["spam", "ham"]