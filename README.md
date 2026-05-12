# Spam Classifier API

A Flask REST API that classifies SMS messages as spam or ham using a Naive Bayes machine learning model trained on the SMS Spam Collection dataset. Send a text message and get back an instant prediction.

---

## Features

- Classifies messages as spam or ham in real time
- Trained on 5,500+ real SMS messages
- REST API built with Flask
- Containerized with Docker for easy deployment
- Automated testing with pytest
- CI/CD pipeline via GitHub Actions

---

## Tech Stack

- **Python** — Core language
- **scikit-learn** — Machine learning (Naive Bayes classifier)
- **Flask** — REST API framework
- **Docker** — Containerization
- **GitHub Actions** — CI/CD pipeline
- **pytest** — Automated testing

---

## Project Structure

```
spam-classifier/
├── app.py                  # Main Flask application
├── train.py                # Model training script
├── model.pkl               # Trained model
├── vectorizer.pkl          # Text vectorizer
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── test_app.py             # Automated tests
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI/CD pipeline
```

---

## How to Run

### Option 1: Run with Docker (Recommended)

Make sure Docker Desktop is installed and running.

```bash
git clone https://github.com/abdullahashrafdev/spam-classifier.git
cd spam-classifier
docker-compose up
```

The API will be live at `http://localhost:5000`

### Option 2: Run Locally

```bash
git clone https://github.com/abdullahashrafdev/spam-classifier.git
cd spam-classifier
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train.py
python app.py
```

---

## API Usage

### Endpoint

```
POST /predict
```

### Request

Send a JSON body with a `text` field.

**Using curl:**
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"Congratulations! You won a free iPhone!\"}"
```

**Using Postman:**
1. Set method to POST
2. URL: `http://localhost:5000/predict`
3. Body → raw → JSON
4. Paste your message and click Send

### Response

```json
{
  "prediction": "spam"
}
```

```json
{
  "prediction": "ham"
}
```

---

## Running Tests

```bash
pytest test_app.py
```

---

## CI/CD Pipeline

Every push to the repository automatically:
1. Builds the Docker image
2. Runs all tests inside the container

Pipeline status is visible under the **Actions** tab on GitHub.

---

## Author

**Muhammad Abdullah**
[github.com/abdullahashrafdev](https://github.com/abdullahashrafdev)
[linkedin.com/in/muhammad-abdullah-a4b59328b](https://www.linkedin.com/in/muhammad-abdullah-a4b59328b)
