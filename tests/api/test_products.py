import allure
import pytest

PRODUCT_FIELDS = {"id", "title", "price", "description", "category", "image"}

CATEGORIES = ["electronics", "jewelery", "men's clothing", "women's clothing"]


@allure.feature("API")
@allure.title("GET /products — 200 и непустой список")
@pytest.mark.api
def test_get_all_products(products_client):
    resp = products_client.list()

    assert resp.status_code == 200
    body = resp.json()
    assert isinstance(body, list)
    assert len(body) > 0


@allure.feature("API")
@allure.title("GET /products/{id} — структура ответа для валидного id")
@pytest.mark.api
def test_get_product_by_id_structure(products_client):
    resp = products_client.get(1)

    assert resp.status_code == 200
    product = resp.json()
    with allure.step("В ответе присутствуют все обязательные поля"):
        assert PRODUCT_FIELDS.issubset(product.keys())
        assert product["id"] == 1


@allure.feature("API")
@allure.title("GET /products/{id} — несуществующий id: 200 с пустым телом (мок)")
@pytest.mark.api
@pytest.mark.parametrize("bad_id", [0, 9999, "abc"])
def test_get_product_nonexistent_id(products_client, bad_id):
    resp = products_client.get(bad_id)

    with allure.step("Статус 200, тело пустое (продукт не отдан)"):
        assert resp.status_code == 200
        assert resp.text == ""


@allure.feature("API")
@allure.title("GET /products/categories — список категорий")
@pytest.mark.api
def test_get_categories(products_client):
    resp = products_client.categories()

    assert resp.status_code == 200
    categories = resp.json()
    assert isinstance(categories, list)
    assert len(categories) > 0
    assert all(isinstance(c, str) and c for c in categories)


@allure.feature("API")
@allure.title("GET /products/category/{category} — фильтр по категории")
@pytest.mark.api
@pytest.mark.parametrize("category", CATEGORIES)
def test_filter_by_category(products_client, category):
    resp = products_client.by_category(category)

    assert resp.status_code == 200
    products = resp.json()
    assert isinstance(products, list)
    assert len(products) > 0
    with allure.step("Каждый товар принадлежит запрошенной категории"):
        assert all(p["category"] == category for p in products)


@allure.feature("API")
@allure.title("GET /products?limit=N — ограничение количества")
@pytest.mark.api
@pytest.mark.parametrize("limit", [1, 5, 10])
def test_limit_parameter(products_client, limit):
    resp = products_client.list(limit=limit)

    assert resp.status_code == 200
    assert len(resp.json()) == limit


@allure.feature("API")
@allure.title("GET /products?sort=desc — порядок по id убыванием")
@pytest.mark.api
def test_sort_desc(products_client):
    resp = products_client.list(sort="desc")

    assert resp.status_code == 200
    ids = [p["id"] for p in resp.json()]
    assert ids == sorted(ids, reverse=True)


@allure.feature("API")
@allure.title("GET /products?sort=asc — порядок по id возрастанием")
@pytest.mark.api
def test_sort_asc(products_client):
    resp = products_client.list(sort="asc")

    assert resp.status_code == 200
    ids = [p["id"] for p in resp.json()]
    assert ids == sorted(ids)


@allure.feature("API")
@allure.title("POST /products — создание возвращает id (201/200)")
@pytest.mark.api
def test_create_product(products_client):
    payload = {
        "title": "Test product",
        "price": 19.99,
        "description": "created in test",
        "image": "https://example.com/img.png",
        "category": "electronics",
    }
    resp = products_client.create(payload)

    assert resp.status_code in (200, 201)
    body = resp.json()
    with allure.step("В ответе есть id и эхо переданных полей"):
        assert "id" in body
        assert body["title"] == payload["title"]


@allure.feature("API")
@allure.title("PUT /products/{id} — обновление")
@pytest.mark.api
def test_update_product_put(products_client):
    payload = {
        "title": "Updated product",
        "price": 29.99,
        "description": "updated in test",
        "image": "https://example.com/img.png",
        "category": "electronics",
    }
    resp = products_client.update(1, payload)

    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == 1
    assert body["title"] == payload["title"]


@allure.feature("API")
@allure.title("PATCH /products/{id} — частичное обновление")
@pytest.mark.api
def test_patch_product(products_client):
    resp = products_client.patch(1, {"title": "Patched title"})

    assert resp.status_code == 200
    body = resp.json()
    with allure.step("Возвращён id и обновлённое поле"):
        assert body["id"] == 1
        assert body["title"] == "Patched title"


@allure.feature("API")
@allure.title("DELETE /products/{id} — удаление")
@pytest.mark.api
def test_delete_product(products_client):
    resp = products_client.delete(1)

    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == 1


@allure.feature("API")
@allure.title("Валидация типов полей товара")
@pytest.mark.api
def test_product_field_types(products_client):
    product = products_client.get(1).json()

    with allure.step("id — int, title — str, category — str"):
        assert isinstance(product["id"], int)
        assert isinstance(product["title"], str)
        assert isinstance(product["category"], str)
    with allure.step("price — число (в данных API встречаются и int, и float)"):
        assert isinstance(product["price"], (int, float))
        assert not isinstance(product["price"], bool)
