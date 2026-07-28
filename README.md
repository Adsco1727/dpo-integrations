# dpo-integrations

Thin Wave-6 integrations orchestration layer that consumes dpo-ledger-tools.

## Scope

- read integration tasks
- validate integration payloads
- apply deterministic integration updates through shared helpers

## Constraints

- thin consumer surface only
- no duplicated ledger logic
- no runtime ledger contamination in tests
DPO ecosystem repository: dpo-integrations
