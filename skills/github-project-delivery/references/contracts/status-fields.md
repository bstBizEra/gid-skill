# Delivery Status Fields

Report these independently; do not infer one from another.

| Field | Meaning |
|---|---|
| `task_state` | Planning, execution, blocked, or declared task boundary |
| `verification_state` | Actual check status for the current candidate |
| `integration_state` | PR and actual merge/integration outcome |
| `runtime_state` | Named environment/deployment outcome and health evidence |
| `business_acceptance` | Acceptance by the accountable owner of the intended outcome |

State the candidate revision, evidence, time, and limitations. A passing local check does not prove integration or production health. A closed Issue does not prove verification or business acceptance.
