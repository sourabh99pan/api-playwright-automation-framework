def test_create_user(api_client):

    payload = {
        "name": "Sourabh",
        "job": "QA Engineer"
    }

    response = api_client.post(
        url="https://jsonplaceholder.typicode.com/users",
        payload=payload
    )

    response_json = response.json()

    print(response_json)

    assert response.status_code == 201

