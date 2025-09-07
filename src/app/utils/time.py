from datetime import datetime, timezone


def nowUtcIso() -> str:
    """Get current UTC time in ISO format."""

    return datetime.now(tz=timezone.utc).isoformat()
