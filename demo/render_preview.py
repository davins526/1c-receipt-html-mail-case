"""Local-only, no transport: demonstrates safe HTML template substitution."""
from html import escape
from pathlib import Path
from string import Template

TEMPLATE = Path(__file__).parent / "templates" / "receipt.html"


def render(data: dict[str, str]) -> str:
    fields = ("account", "address", "period", "amount", "due_date", "organization")
    missing = [name for name in fields if name not in data]
    if missing:
        raise ValueError("Missing fields: " + ", ".join(missing))
    encoded = {field: escape(str(data[field]), quote=True) for field in fields}
    return Template(TEMPLATE.read_text(encoding="utf-8")).substitute(encoded)


def main():
    fake = {
        "account": "FAKE-0001", "address": "ул. Учебная, д. 10, кв. 1",
        "period": "Апрель 2026", "amount": "123,45 ₽", "due_date": "до 10.05.2026",
        "organization": "Демонстрационная организация",
    }
    path = Path(__file__).parent / "preview.html"
    path.write_text(render(fake), encoding="utf-8")
    print(f"Preview (no email sent): {path}")


if __name__ == "__main__":
    main()
