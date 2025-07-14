import torch
from torchvision import models, transforms
from PIL import Image

# Load model
model = models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(model.fc.in_features, 2)  # binary classifier
model.load_state_dict(torch.load("models/resnet18_phish.pt", map_location="cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict_image(img_path: str) -> str:
    image = Image.open(img_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        logits = model(input_tensor)
        prob = torch.softmax(logits, dim=1)
    label = "phishing" if torch.argmax(prob) == 1 else "legit"
    return label, float(prob[0][1])
