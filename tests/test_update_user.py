def test_update_user(api_client):

    payload = {
        "name": "Sourabh Updated",
        "job": "Senior QA Engineer"
    }

    response = api_client.put(
        url="https://jsonplaceholder.typicode.com/users/1",
        payload=payload
    )

    response_json = response.json()

    print(response_json)

    assert response.status_code == 200

    assert response_json["name"] == "Sourabh Updated"

    assert response_json["job"] == "Senior QA Engineer"