import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    image_link_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_link_pattern, text)
    return matches


def extract_markdown_links(text):
    link_pattern = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_pattern, text)
    return matches

    
