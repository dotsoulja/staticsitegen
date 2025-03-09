import unittest
from textnode import TextNode, TextType
from inlinetext import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_text(self):
        nodes = text_to_textnodes(
            "This has a **bold** word, an _italic_ word, some `code`, and an ![image](https://www.google.com)"
             "and a [link](https://www.google.com)"    
        )

        self.assertListEqual(
            [
                TextNode("This has a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word, an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word, some ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(", and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://www.google.com"),
                TextNode("and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
            ],
            nodes,
        )

if __name__ == "__main__":
    unittest.main()