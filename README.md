# ML Phishing Page Detection
Classify screenshots or DOM data of login pages to identify fake sites phishing for credentials.

---

## Project Overview
Automatically detect phishing websites that mimic legitimate login pages (e.g., banking, email, social media) by analyzing their visual appearance, HTML structure, and textual content.

---

## Goals
1. Detect fake login pages in real time and with high precision
2. Leverage visual, structural, and semantic features for robust detection
3. Optional browser extension or SOC dashboard for alerting

---

## Architecture & Workflow
```plaintext
            ┌────────────┐
            │  Target URL│
            └─────┬──────┘
                  ▼
       ┌────────────────────┐
       │ Page Renderer (Headless) │  ← Screenshots, HTML dump
       └────────┬───────────┘
                ▼
   ┌────────────┴─────────────┐
   │ Feature Extractor        │
   │ ├── Visual: screenshot   │ ← CNN-based classifier
   │ ├── Text: NLP on content │ ← BERT, TF-IDF, etc.
   │ └── DOM: tag structure   │ ← tag frequency, depth
   └────────────┬─────────────┘
                ▼
       ┌────────┴────────┐
       │   ML Classifier │ ← binary classification: {real, fake}
       └────────┬────────┘
                ▼
        ┌───────┴────────┐
        │ Alert/Block/Log│
        └────────────────┘
```

---

## Tech Stack
```plaintext
| Area                     | Tool/Library                              | Purpose                                           |
| ------------------------ | ----------------------------------------- | ------------------------------------------------- |
| **Web Scraping**         | `Playwright` / `Selenium`                 | Load page, take screenshots, extract HTML         |
| **Image Classification** | `PyTorch` / `TensorFlow`                  | CNN model to classify page screenshots            |
| **Text Analysis**        | `Transformers (BERT)`                     | Analyze textual clues (e.g., "Login to PayPal")   |
| **DOM Analysis**         | `BeautifulSoup`, `lxml`                   | Parse HTML, extract structural features           |
| **Model Training**       | `scikit-learn`, `XGBoost`                 | Traditional models on structural/textual features |
| **Monitoring**           | `FastAPI`, `Prometheus`                   | Optional API and alerting layer                   |
| **Deployment**           | `Docker`, `Kubernetes`                    | Serve the model in a scalable microservice        |
| **Dataset Sources**      | PhishTank, OpenPhish, Legit scraped pages | Collect real vs. phishing pages                   |
```

---

## Features 
- Visual
  - Screenshot image (CNN input)
  - Logo detection (optional)
  - Layout similarities
- Textual
  - Login-related keywords
  - Brand mentions (e.g., PayPal, Google)
  - Language models for semantic similarity
- DOM Structure
-   <input type=password> presence
-   Form actions, external links
-   Suspicious domains in href attributes

---

## Output
The final model returns:
```json
{
  "label": "phishing",
  "confidence": 0.96,
  "explanation": "Fake PayPal login on suspicious domain"
}

```
