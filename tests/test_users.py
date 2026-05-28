def test_get_users(api_client):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response_json = response.json()

    print(response_json)

    assert response.status_code == 200

    assert response.text != ""

def test_get_users_content_type(api_client):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status_code == 200

    assert "application/json" in response.headers["Content-Type"]

def test_get_users_keys_validation(api_client):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response_json = response.json()

    first_user = response_json[0]

    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user
    assert "username" in first_user

def test_get_users_datatypes(api_client):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response_json = response.json()

    first_user = response_json[0]

    assert isinstance(first_user["id"], int)

    assert isinstance(first_user["name"], str)

    assert isinstance(first_user["email"], str)

def test_get_users_response_time(api_client):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response_json = response.json()

    assert response.elapsed.total_seconds() < 2

    assert len(response_json) == 10

def test_get_specific_user_values(api_client):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status_code == 200

    response_json = response.json()

    first_user = response_json[0]

    assert first_user["id"] == 1

    assert first_user["name"] == "Leanne Graham"

    assert first_user["username"] == "Bret"

    assert first_user["email"] == "Sincere@april.biz"

    assert first_user["phone"] == "1-770-736-8031 x56442"

    assert first_user["website"] == "hildegard.org"

    assert first_user["address"]["city"] == "Gwenborough"

    assert first_user["address"]["street"] == "Kulas Light"