import requests

# 安装：pip install requests


# GET请求
def simple_get():
    response = requests.get("https://httpbin.org/get")
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
    print(f"JSON响应: {response.json()}")


simple_get()


# POST请求
def simple_post():
    # 表单数据
    data = {"username": "test", "password": "123456"}
    response = requests.post("https://httpbin.org/post", data=data)

    # JSON数据
    json_data = {"name": "John", "age": 30}
    response = requests.post("https://httpbin.org/post", json=json_data)

    print(response.json())


# 带参数的GET请求
def get_with_params():
    params = {"page": 1, "limit": 20, "keyword": "python"}
    response = requests.get("https://httpbin.org/get", params=params)
    print(f"请求URL: {response.url}")
    print(f"响应: {response.json()}")
