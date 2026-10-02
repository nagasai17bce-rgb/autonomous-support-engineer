# Autonomous Support Engineer

A support-triage API that classifies incidents, proposes a deterministic diagnostic sequence, and escalates urgent production failures.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

The design intentionally separates diagnosis from remediation so production actions can require approval.

## Production extensions
Connect ticketing, observability, incident history, ownership metadata, runbooks, and approval-gated remediation tools.
