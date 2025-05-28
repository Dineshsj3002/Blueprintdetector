import requests

url = "http://127.0.0.1:8000/detect"
file_path = r"C:\Users\sjdin\OneDrive\Documents\aitask\blueprint-detector\images\train\2.png"


with open(file_path, "rb") as f:
    response = requests.post(url, files={"file": f})
    print("Status code:", response.status_code)
    try:
        print("JSON response:", response.json())
    except Exception as e:
        print("Error parsing JSON:", str(e))
        print("Response text:", response.text)
