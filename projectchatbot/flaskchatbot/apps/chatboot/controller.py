
import requests

api_key = "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"

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {api_key}"}

def query(text):
    
    payload = {
        'inputs': f"""{text}"""
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	


if __name__ == '__main__':
    input_text = "Can you please let us know more details about your."
    output = query(input_text)
    print(output)
