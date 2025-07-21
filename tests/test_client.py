import pytest
import requests
import requests_mock
from marketplace_sdk import MarketplaceClient
from marketplace_sdk.exceptions import MarketplaceAPIError

BASE_URL = "http://localhost:5565"

@pytest.fixture
def client():
    return MarketplaceClient(base_url=BASE_URL)

def test_register_agent_success(client):
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/agents/", json={"result": "ok"}, status_code=200)
        resp = client.register_agent("TestAgent", "http://localhost:9999")
        assert resp["result"] == "ok"

def test_register_agent_failure(client):
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/agents/", text="Bad Request", status_code=400)
        with pytest.raises(MarketplaceAPIError):
            client.register_agent("TestAgent", "http://localhost:9999")

def test_discover_agents_success(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}/agents/", json={"agents": ["A1", "A2"]}, status_code=200)
        resp = client.discover_agents()
        assert "agents" in resp

def test_request_agent_success(client):
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/agents/", json={"response": "42"}, status_code=200)
        resp = client.request_agent("A1", "What is the answer?")
        assert resp["response"] == "42" 