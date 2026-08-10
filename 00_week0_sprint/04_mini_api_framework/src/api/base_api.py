"""HTTP-клиент. Реализуй по TASK.md."""
import requests

class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str, expected_status: int = 200) -> dict:
        full_url = self.base_url + path
        r = requests.get(url=full_url, headers={"User-Agent": "Mozilla/5.0","content-type": "application/json"})
        assert r.status_code == expected_status, f"Ожидали статус код{expected_status}, пришел {r.status_code}"
        return r.json()