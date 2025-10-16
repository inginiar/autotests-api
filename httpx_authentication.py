import httpx
#
# data = {
#   "email": "user@example.com",
#   "password": "string",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string"
# }
#
# response = httpx.post("http://localhost:8000/api/v1/users", json=data)
#
# print(response.status_code)

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()


print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

refresh_payload = {
    "refreshToken": login_response_data['token']['refreshToken']
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
