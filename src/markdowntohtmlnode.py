from enum import Enum
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode
from blocktype import block_to_block_type, BlockType
from markdownblocks import markdown_to_blocks
from inlinetext import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    children = []
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
         return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    raise ValueError(f"Unknown block type: {block_type}")
    

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    while block[level] == "#":
        level += 1
    children = text_to_children(block[level + 1:])
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_line_list = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_line_list.append(line.lstrip("> ").strip())
    content = " ".join(new_line_list)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        text = line.lstrip("- ").strip()
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)

def ordered_list_to_html_node(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)
