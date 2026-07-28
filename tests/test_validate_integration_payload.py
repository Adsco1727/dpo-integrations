import pytest
from dpo_integrations.payloads import validate_integration_payload


def test_valid_integration_payload():
    assert validate_integration_payload({"task_id": "I123", "action": "sync"}) is True


def test_missing_fields_fail():
    with pytest.raises(Exception):
        validate_integration_payload({"task_id": "I123"})
