import requests
import time

start_time = time.time()
response = requests.get("http://www.google.com")
end_time = time.time()
print(f"Статус-код: {response.status_code}")
print(f"Тип содержимого: {response.headers.get('Content-type')}")
print(f"Размер контента: {response.headers.get('Content-Length')} байт")
print(f"Время ответа: {end_time - start_time} секунд")


