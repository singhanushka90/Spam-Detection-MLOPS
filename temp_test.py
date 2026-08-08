import requests
payload = {'username':'testuser','email':'testuser@example.com','password':'12345678'}
r = requests.post('http://127.0.0.1:8002/auth/register', json=payload, timeout=10)
print('status', r.status_code)
print(r.text)
