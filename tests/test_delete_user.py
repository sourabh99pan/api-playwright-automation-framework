def test_delete_user(api_client):

    response = api_client.delete(
        url="https://jsonplaceholder.typicode.com/users/1"
    )

    print(response.status_code)

    assert response.status_code == 200