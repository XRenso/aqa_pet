import pytest

from clients.products_client import ProductsClient


@pytest.fixture
def products_client(api_base_url):
    """Готовый клиент /products"""
    return ProductsClient(api_base_url)
