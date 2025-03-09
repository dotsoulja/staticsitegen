import unittest
from textnode import TextNode, TextType
from markdownlinks import extract_markdown_images, extract_markdown_links
from inlinetext import split_nodes_images, split_nodes_links




class TestMarkdownLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://www.google.com)"
        )

        self.assertListEqual([("image", "https://www.google.com")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )

        self.assertListEqual([("link", "https://www.google.com")], matches)


    

if __name__ == "__main__":
    unittest.main()