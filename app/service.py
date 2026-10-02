class Service:
    def run(self, value: str):
        urgent = any(x in value.lower() for x in ("down", "blocked", "production"))
        return {
            "ticket": value,
            "priority": "high" if urgent else "normal",
            "diagnosis_steps": ["classify", "retrieve incidents", "check recent changes", "draft remediation"],
            "escalate": urgent,
        }
