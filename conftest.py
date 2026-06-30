import pytest

from config import API_BASE_URL


@pytest.fixture(scope="session")
def api_base_url():
    return API_BASE_URL


@pytest.fixture
def context(context):
    """Блокировка рекламы"""

    ad_patterns = (
        "**/*googleads*/**",
        "**/*doubleclick*/**",
        "**/*googlesyndication*/**",
    )
    for pattern in ad_patterns:
        context.route(pattern, lambda route: route.abort())

    yield context
