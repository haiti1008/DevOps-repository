import requests
from PIL import Image
import sys

print(f"Python versie: {sys.version}")
print(f"Requests versie: {requests.__version__}")

response = requests.get("https://httpbin.org/get")
print(f"HTTP status: {response.status_code}")
print("Virtual environment werkt correct!")

