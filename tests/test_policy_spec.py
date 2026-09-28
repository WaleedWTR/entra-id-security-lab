import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "policies" / "conditional-access-baseline.json"

def load_spec():
    return json.loads(SPEC.read_text(encoding="utf-8"))

def test_policy_ids_are_unique():
    policies = load_spec()["policies"]
    ids = [p["id"] for p in policies]
    assert len(ids) == len(set(ids))

def test_portfolio_policies_start_in_report_only():
    for policy in load_spec()["policies"]:
        assert policy["state"] == "reportOnly"

def test_privileged_policies_keep_emergency_access_exclusion():
    privileged = [
        p for p in load_spec()["policies"]
        if "privileged-administrators" in p["scope"]["personas"]
    ]
    assert privileged
    assert all(
        "emergency-access-accounts" in p["scope"]["exclusions"]
        for p in privileged
    )
