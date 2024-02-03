import requests
import json

def do_request():
    url = "https://api.baichuan-ai.com/v1/chat/completions"
    api_key = "your_api_key"

    data = {
        "model": "Baichuan2-Turbo",
        "messages": [
            {
                "role": "user",
                "content": "世界第一高峰是"
            }
        ],
        "stream": True
    }

    json_data = json.dumps(data)

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    response = requests.post(url, data=json_data, headers=headers, timeout=60)

    if response.status_code == 200:
        print("请求成功！")
        print("响应body:", response.text)
        print("请求成功，X-BC-Request-Id:", response.headers.get("X-BC-Request-Id"))
    else:
        print("请求失败，状态码:", response.status_code)
        print("请求失败，body:", response.text)
        print("请求失败，X-BC-Request-Id:", response.headers.get("X-BC-Request-Id"))

if __name__ == "__main__":
    do_request()

              