import unittest
from generatesite import extract_title


class TestGenerateSite(unittest.TestCase):
    def test_extract_title(self):
        sample_markdown = "# sample markdown title"
        title = extract_title(sample_markdown)
        self.assertEqual("sample markdown title", title)

    
    def test_extract_title_no_title(self):
        sample_markdown = "sample markdown title"
        with self.assertRaises(ValueError):
            extract_title(sample_markdown)

    def test_extract_title_with_trailing_whitespace(self):
        sample_markdown = "# sample markdown title "
        title = extract_title(sample_markdown)
        self.assertEqual("sample markdown title", title)

    def test_extract_title_with_other_headers(self):
        sample_markdown = "# This is a title\n## this should not be extracted"
        title = extract_title(sample_markdown)
        self.assertEqual("This is a title", title)

