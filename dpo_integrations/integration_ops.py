from .payloads import validate_integration_payload


class IntegrationOps:
    def __init__(self, ledger_api, sheet_writer=None):
        self.ledger_api = ledger_api
        self.sheet_writer = sheet_writer

    def read_integration_tasks(self):
        rows = self.ledger_api.read_rows("INGESTION_QUEUE")
        tasks = []
        for row in rows:
            tasks.append(
                {
                    "task_id": row.get("batch_id"),
                    "action": row.get("ingestion_type", "sync"),
                    "status": row.get("status", "pending"),
                    "source_repo": row.get("source_repo", ""),
                }
            )
        return tasks

    def apply_integration_update(self, payload: dict):
        validate_integration_payload(payload)

        if self.sheet_writer is not None:
            self.sheet_writer("INTEGRATION_QUEUE", payload)
            return True

        updates = {
            "status": "running" if payload.get("action") == "sync" else "pending",
            "notes": "integration_action={}".format(payload.get("action", "sync")),
        }
        self.ledger_api.update_row("INGESTION_QUEUE", "batch_id", payload["task_id"], updates)
        return True
