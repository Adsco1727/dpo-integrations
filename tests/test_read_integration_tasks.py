def test_can_read_integration_tasks():
    from dpo_integrations.integration_ops import IntegrationOps

    class FakeLedgerApi:
        def read_rows(self, sheet):
            assert sheet == "INGESTION_QUEUE"
            return [{"batch_id": "I123", "ingestion_type": "sync", "status": "pending", "source_repo": "x"}]

    api = FakeLedgerApi()
    ops = IntegrationOps(api, None)

    rows = ops.read_integration_tasks()
    assert rows[0]["task_id"] == "I123"
