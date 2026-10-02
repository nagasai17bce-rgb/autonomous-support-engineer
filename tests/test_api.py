from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_urgent_ticket(): assert client.post("/v1/run",json={"value":"production is down"}).json()["escalate"] is True
