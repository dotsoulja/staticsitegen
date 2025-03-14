import os
import shutil
from markdowntohtmlnode import markdown_to_html_node


def extract_title(markdown):
    """"
    Extracts the h1 title from a markdown file (string), stripping the # and any leading/trailing whitespace."
    if no h1 title is found, raise an exception."
    """
    lines = markdown.split("\n")
    if not lines[0].startswith("# "):
        raise ValueError("No h1 title found")
    title = lines[0][2:].strip()
    print(f"{title}")
    return title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template: {template_path}")

    # read the markdown file and store contents in variable
    with open(from_path, "r") as file:
        markdown_content = file.read()
    # read the template file and store contents in variable
    with open(template_path, "r") as file:
        template = file.read()

    # use markdown_to_html_node function and .to_html() method to convert markdown to html
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    # replace the title and body in the template with the title and html content
    template = template.replace("{{ title }}", title)
    template = template.replace("{{ body }}", html)

    # write the new html content to the destination path
    destination_dir_path = os.path.dirname(dest_path)
    if destination_dir_path != "":
        os.makedirs(destination_dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)
    print(f"Page generated at {dest_path}")
    
     
    