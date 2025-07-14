from bs4 import BeautifulSoup

def extract_features_from_html(html_file: str):
    with open(html_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    features = {
        "has_password_input": bool(soup.find("input", {"type": "password"})),
        "has_login_keyword": any(word in soup.text.lower() for word in ["login", "signin", "account", "verify"]),
        "has_brand_mention": any(word in soup.text.lower() for word in ["paypal", "bank", "apple", "google"]),
    }
    return features
