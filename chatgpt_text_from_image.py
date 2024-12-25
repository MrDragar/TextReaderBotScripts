import requests
import json


def handle(data):
    data = json.loads(data)
    api_key = data["CHATGPT_API_KEY"]
    proxy = {
        "https": data["HTTPS_PROXY"]
    }
    image_url = data["image_url"]
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Write me text, which is in this picture. WRITE ONLY TEXT, DO NOT ADD ANYTHING YOURSELF"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url":  image_url
                        },
                    },
                ],
            }
        ],
        "max_tokens": 300,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data),
                             proxies=proxy)

    if response.status_code == 200:
        return response.json()['choices'][0]["message"]["content"]
    else:
        return

