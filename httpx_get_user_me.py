import httpx


login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)
print(access_token)

headers = {"Authorization": f'Bearer {access_token}'}

get_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
data = get_response.json()

print("Status Code", get_response.status_code)
print("Get response:", data)