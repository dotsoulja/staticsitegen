import os
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


def generate_page(from_path, template_path, dest_path, basepath):
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
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # replace all instances of href="/ with href="{BASEPATH}
    template = template.replace('href="/', 'href="' + basepath)
    # replace all instances of src="/ with src="{BASEPATH}
    template = template.replace('src="/', 'src="' + basepath)

    # write the new html content to the destination path
    destination_dir_path = os.path.dirname(dest_path)
    if destination_dir_path != "":
        os.makedirs(destination_dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)
    print(f"Page generated at {dest_path}")
    
     

# function that generates pages recursively
def generate_pages_recursive(from_path, template_path, dest_path, basepath):
    print(f"Generating pages from {from_path} to {dest_path} using template: {template_path}")
    # check if the from_path is a file
    if os.path.isfile(from_path):
        generate_page(from_path, template_path, dest_path, basepath)
    # check if the from_path is a directory
    elif os.path.isdir(from_path):
        # loop through all the files in the directory
        for file_name in os.listdir(from_path):
            # create the full path of the file
            full_path = os.path.join(from_path, file_name)
            # create the destination path
            new_dest_path = os.path.join(dest_path, file_name.replace(".md", ".html"))
            # recursively call the function
            generate_pages_recursive(full_path, template_path, new_dest_path, basepath)
    else:
        raise ValueError(f"{from_path} is not a valid file or directory")
    print(f"Finished generating pages from {from_path} to {dest_path}")