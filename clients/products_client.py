import allure
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class ProductsClient:
    """
    Клиент для /products Fake Store API
    """

    TIMEOUT = 30

    # Cloudflare за fakestoreapi режет дефолтный python-requests UA (403 на CI-IP)
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json",
    }

    def __init__(self, base_url: str, session: requests.Session = None):
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
        self.session.headers.update(self.HEADERS)
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=(502, 503, 504),
            allowed_methods=("GET", "POST", "PUT", "PATCH", "DELETE"),
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def _url(self, path: str = "") -> str:
        return f"{self.base_url}/products{path}"

    @allure.step("GET /products")
    def list(self, **params) -> requests.Response:
        return self.session.get(
            self._url(), params=params or None, timeout=self.TIMEOUT
        )

    @allure.step("GET /products/{product_id}")
    def get(self, product_id) -> requests.Response:
        return self.session.get(self._url(f"/{product_id}"), timeout=self.TIMEOUT)

    @allure.step("GET /products/categories")
    def categories(self) -> requests.Response:
        return self.session.get(self._url("/categories"), timeout=self.TIMEOUT)

    @allure.step("GET /products/category/{category}")
    def by_category(self, category: str) -> requests.Response:
        return self.session.get(
            self._url(f"/category/{category}"), timeout=self.TIMEOUT
        )

    @allure.step("POST /products")
    def create(self, payload: dict) -> requests.Response:
        return self.session.post(self._url(), json=payload, timeout=self.TIMEOUT)

    @allure.step("PUT /products/{product_id}")
    def update(self, product_id, payload: dict) -> requests.Response:
        return self.session.put(
            self._url(f"/{product_id}"), json=payload, timeout=self.TIMEOUT
        )

    @allure.step("PATCH /products/{product_id}")
    def patch(self, product_id, payload: dict) -> requests.Response:
        return self.session.patch(
            self._url(f"/{product_id}"), json=payload, timeout=self.TIMEOUT
        )

    @allure.step("DELETE /products/{product_id}")
    def delete(self, product_id) -> requests.Response:
        return self.session.delete(self._url(f"/{product_id}"), timeout=self.TIMEOUT)
