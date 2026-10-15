# G05 — Agents and handoffs

**Trigger:** Delegate work, switch runtime/provider, or resume another agent's task.
**Inputs:** Task scope, current candidate, authority, files/resources, attempt ledger, verification and unresolved decisions.
**Capability assumptions:** Delegation, shared files, and provider tools are used only when available and authorized.
**Actions:** Confirm runtime capabilities; assign one writer per shared scope; provide bounded inputs and acceptance criteria; preserve history, evidence, and budget; review returned work before integration.
**Output:** Provider-neutral execution or handoff packet.
**Exit and recovery:** If delegation is unavailable or unauthorized, continue sequentially. On interrupted work, resume from the recorded candidate and ledger.
**Authority limit:** Delegation does not grant the recipient additional write, merge, release, or deployment authority.
