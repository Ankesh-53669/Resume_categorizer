import requests

url = "http://127.0.0.1:5000/predict"
file_path = "10001727.pdf"

# Open the PDF file
with open(file_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

# Print the response
print(response.json())
