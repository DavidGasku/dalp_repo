'''
Mi programa
'''
import requests

major_version = 0
minor_version = 5
patch_version = 1

print(f"Version {major_version}.{minor_version}.{patch_version}")

respuesta = requests.get("https://httpbin.org/get")
print(f"Status: {respuesta.status_code}")
print(f"IP: {respuesta.json()['origin']}")
