import os
import json
from jinja2 import Environment, FileSystemLoader

# Define the directory containing subdirectories with RO-Crate files
base_dir = 'roCrates'
gh_pages_dir = 'gh_pages'

# Set up Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('ro-crate-preview-template.html.jinja')

# Iterate over each subdirectory in the base directory
for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)

    # Check if the path is a directory
    if os.path.isdir(subdir_path):
        # Define the expected RO-Crate metadata file path
        crate_file_path = os.path.join(subdir_path, 'ro-crate-metadata.json')

        # Check if the RO-Crate file exists in the subdirectory
        if os.path.exists(crate_file_path):
            # Load RO-Crate data
            with open(crate_file_path) as crate_file:
                crate_data = json.load(crate_file)

            # Convert crate_data to JSON-LD formatted string
            crate_json_ld = json.dumps(crate_data, indent=2)

            # Extract the graph data for dynamic table generation
            graph = crate_data.get('@graph', [])

            # Render the template with data, including the JSON-LD string
            rendered_html = template.render(crate_json_ld=crate_json_ld, graph=graph)

            output_html_path = os.path.join(subdir_path, 'ro-crate-preview.html')
            print(output_html_path)
            pages_html_path = os.path.join(gh_pages_dir, f'ro-crate-preview-{subdir}.html')
            print(pages_html_path)

            # Save the rendered HTML to a file
            with open(output_html_path, 'w') as output_file:
                output_file.write(rendered_html)

            # Save the rendered HTML in gh-pages directory
            with open(pages_html_path, 'w') as output_file:
                output_file.write(rendered_html)

            print(f"HTML page has been generated: {output_html_path} and {pages_html_path}")
        else:
            print(f"No RO-Crate file found in: {subdir_path}")
