from textnode import TextNode, TextType
from copystatic import copy_static_recursive

def main():
    node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")
    print(node)


    print("starting copy_static_recursive")
    copy_static_recursive("./static", "./public")
    print("finished copy_static_recursive")

main()
