import unittest
from htmlnode import HTMLNode, LeafNode


class TestLeafNode(unittest.TestCase):
    
    def test_leaf_to_html(self):
        node = LeafNode("p", "This is a test paragraph")
        self.assertEqual(
            node.to_html(),
            "<p>This is a test paragraph</p>",
        )

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click on me!", {"href": "https://www.boot.dev"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.boot.dev">Click on me!</a>',
        )

    def test_leaf_to_html_no_value(self):
        node = LeafNode("a", None, {"href": "https://www.boot.dev"})
        with self.assertRaises(ValueError):
            node.to_html()
    

if __name__ == "__main__":
    unittest.main()