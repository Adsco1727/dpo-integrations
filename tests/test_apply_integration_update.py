def test_can_apply_integration_update_deterministically():
    written = []

    def fake_writer(sheet, payload):
        written.append((sheet, payload))

    class FakeLedgerApi:
        def read_rows(self, sheet):
            return []

    from dpo_integrations.integration_ops import IntegrationOps

    api = FakeLedgerApi()
    ops = IntegrationOps(api, fake_writer)

    payload = {"task_id": "I123", "action": "sync"}
    assert ops.apply_integration_update(payload) is True
    assert written[0][0] == "INTEGRATION_QUEUE"
