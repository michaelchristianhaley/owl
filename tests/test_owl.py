import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import owl


class OwlProjectTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        templates = Path(__file__).resolve().parents[1] / "templates"
        for name in owl.OWL_FILES:
            shutil.copyfile(templates / name, self.root / name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid_project(self):
        messages = owl.validate_project(self.root)
        self.assertTrue(any("continuity" in item for item in messages))

    def test_missing_file_fails(self):
        (self.root / "WISDOM.md").unlink()
        with self.assertRaises(owl.OwlError):
            owl.validate_project(self.root)

    def test_missing_outline_section_fails(self):
        path = self.root / "OUTLINE.md"
        text = path.read_text(encoding="utf-8").replace("## Next action", "## Later")
        path.write_text(text, encoding="utf-8")
        with self.assertRaises(owl.OwlError):
            owl.validate_project(self.root)

    def test_empty_objective_fails(self):
        path = self.root / "OUTLINE.md"
        text = path.read_text(encoding="utf-8")
        start = text.index("## Current objective")
        end = text.index("## Verified current state")
        path.write_text(text[:start] + "## Current objective\n\n" + text[end:], encoding="utf-8")
        with self.assertRaises(owl.OwlError):
            owl.validate_project(self.root)


class OwlboxTests(unittest.TestCase):
    def test_self_check(self):
        root = Path(__file__).resolve().parents[1]
        owl.generate(root)
        messages = owl.validate_self(root)
        self.assertTrue(any("generated views" in item for item in messages))


if __name__ == "__main__":
    unittest.main()
