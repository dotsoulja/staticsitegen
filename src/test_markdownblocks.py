import unittest
from markdownblocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is a **bolded** word

and a new paragraph with an _italic_ word
and another line of same paragraph

and a new paragraph with some `code block` in it

- This is a list
- with some items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** word",
                "and a new paragraph with an _italic_ word\nand another line of same paragraph",
                "and a new paragraph with some `code block` in it",
                "- This is a list\n- with some items",
            ],
        )

    def test_block_to_block_type(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block1 = "```\nThis is code\n```"
        self.assertEqual(block_to_block_type(block1), BlockType.CODE)
        block = "> This has a quote\n> with multiple lines"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- This is a list\n- with some items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. This is a list\n2. with some items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()