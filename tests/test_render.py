import unittest
from demo.render_preview import render

FAKE = {"account": "FAKE-0001", "address": "ул. Учебная, 1", "period": "Апрель 2026",
        "amount": "123,45 ₽", "due_date": "до 10.05.2026", "organization": "Демо"}


class RenderTests(unittest.TestCase):
    def test_renders_expected_fields(self):
        result = render(FAKE)
        self.assertIn("FAKE-0001", result)
        self.assertIn("123,45 ₽", result)

    def test_escapes_html(self):
        injected = {**FAKE, "address": '<script>alert("x")</script>'}
        result = render(injected)
        self.assertNotIn("<script>", result)
        self.assertIn("&lt;script&gt;", result)

    def test_required_field(self):
        short = {key: value for key, value in FAKE.items() if key != "amount"}
        with self.assertRaises(ValueError):
            render(short)


if __name__ == "__main__":
    unittest.main()
