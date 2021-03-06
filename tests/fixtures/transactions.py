import pytest


@pytest.fixture
def minimal():
    return {
        "service": {
            "name": "service1",
            "agent": {
                "name": "python",
                "version": "1.0"
            }
        },
        "transactions": [
            {
                "id": "945254c5-67a5-417e-8a4e-aa29efcbfb79",
                "name": "GET /api/types",
                "type": "request",
                "duration": 32.592981,
                "result": "success",
                "timestamp": "2017-05-09T15:04:05.999999Z"
            }
        ]
    }
