from authority_drift_training.api_requester import ApiRequester


def test_default_timeout():
    requester = ApiRequester(timeout=30)
    assert requester.timeout == 30


def test_default_retry_enabled():
    requester = ApiRequester(timeout=30)
    assert requester.retry is True


def test_retry_can_be_disabled():
    requester = ApiRequester(timeout=30, retry=False)
    assert requester.retry is False


def test_timeout_setter():
    requester = ApiRequester(timeout=30)
    requester.timeout = 60
    assert requester.timeout == 60


def test_curl_cmd_get():
    requester = ApiRequester(timeout=30)
    cmd = requester._curl_cmd(
        url="https://api.example.com/paper",
        parameters="fields=title",
        method="GET",
        headers={"x-api-key": "test123"},
    )
    assert "curl -X GET" in cmd
    assert "https://api.example.com/paper" in cmd
    assert "fields=title" in cmd
    assert "x-api-key: test123" in cmd
