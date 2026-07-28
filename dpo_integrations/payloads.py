from .errors import IntegrationError


def validate_integration_payload(payload: dict):
    if "task_id" not in payload:
        raise IntegrationError("Missing task_id")
    if "action" not in payload:
        raise IntegrationError("Missing action")
    return True
