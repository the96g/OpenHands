"""Trusted runtime flags for Arnau's DGX deployment.

This helper intentionally loosens default safety checks for self-hosted,
fully isolated environments. Do **not** enable in shared or untrusted setups;
with the flag disabled, behavior remains identical to upstream OpenHands.
"""

import os
from functools import lru_cache


@lru_cache(maxsize=1)
def is_dgx_trusted_runtime() -> bool:
    """
    Returns True when running in Arnau's private DGX environment.

    Controlled via env var OPENHANDS_DGX_TRUST_RUNTIME.
    This is ONLY for self-hosted, fully isolated environments.
    """
    return os.getenv("OPENHANDS_DGX_TRUST_RUNTIME", "").lower() in {
        "1",
        "true",
        "yes",
        "on",
    }
