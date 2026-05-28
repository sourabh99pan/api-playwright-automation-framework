def test_401_unauthorized(api_client):

    response = api_client.get(
        "https://httpbin.org/status/401"
    )

    assert response.status_code == 401


def test_403_forbidden(api_client):

    response = api_client.get(
        "https://httpbin.org/status/403"
    )

    assert response.status_code == 403


def test_404_not_found(api_client):

    response = api_client.get(
        "https://httpbin.org/status/404"
    )

    assert response.status_code == 404


def test_429_rate_limit(api_client):

    response = api_client.get(
        "https://httpbin.org/status/429"
    )

    assert response.status_code == 429


def test_500_internal_server_error(api_client):

    response = api_client.get(
        "https://httpbin.org/status/500"
    )

    assert response.status_code == 500


def test_503_service_unavailable(api_client):

    response = api_client.get(
        "https://httpbin.org/status/503"
    )

    assert response.status_code == 503