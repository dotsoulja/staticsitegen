import sys
from copystatic import copy_static_recursive
from generatesite import generate_page, generate_pages_recursive




source_dir = "./static"
new_dir = "./docs"
content_dir = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("starting copy_static_recursive")
    copy_static_recursive(source_dir, new_dir)
    print("finished copy_static_recursive")

    print(f"Generating site from {content_dir} to {new_dir} using template: {template_path}")
    # use the generate_pages_recursive function to generate the site
    generate_pages_recursive(content_dir, template_path, new_dir, basepath)

    print("Finished generating site")


main()
