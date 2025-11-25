# OpenHands DGX trusted runtime flag

Set `OPENHANDS_DGX_TRUST_RUNTIME=1` to enable the trusted runtime mode intended for Arnau's private, self-hosted DGX deployment. In this mode OpenHands bypasses confirmation gating for high-risk tool calls (for example `execute_bash`) while logging a warning. Leave the flag unset in untrusted or multi-tenant environments to retain the default upstream safety behavior.
