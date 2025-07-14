from src.model_cnn import predict_image
from src.features import extract_features_from_html

def predict_url(path="output/"):
    label, score = predict_image(f"{path}/page.png")
    features = extract_features_from_html(f"{path}/page.html")

    print(f"[CNN] Prediction: {label} ({score:.2f})")
    print("[DOM Features]:", features)

    if label == "phishing" or (features["has_password_input"] and features["has_login_keyword"] and not features["has_brand_mention"]):
        verdict = "phishing"
    else:
        verdict = "legit"

    return {
        "label": verdict,
        "cnn_score": score,
        "features": features
    }
