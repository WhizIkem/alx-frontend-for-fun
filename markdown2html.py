#!/usr/bin/python3
"""
Script markdown2html.py that takes an argument 2 strings:
    first argument is the name of the markdown file
    second argument is the output file name
Parse Markdown headings and return corresponding HTML
"""
import sys
import os
import re


def parse_line(line):
    # Check for headings
    match_heading = re.match(r'(#+) (.+)', line)
    if match_heading:
        level = len(match_heading.group(1))
        content = match_heading.group(2)
        return f"<h{level}>{content}</h{level}>"

    # Check for unordered list items
    match_list_item = re.match(r'- (.+)', line)
    if match_list_item:
        content = match_list_item.group(1)
        return f"<li>{content}</li>"

    return line


def markdown_to_html(filename):
    # Convert markdown content to HTML
    with open(filename, 'r') as f:
        lines = f.readlines()

    html_lines = []
    inside_ul = False

    for line in lines:
        line = line.strip()
        if line.startswith("- "):
            if not inside_ul:
                inside_ul = True
                html_lines.append("<ul>")
            html_lines.append(parse_line(line))
        else:
            if inside_ul:
                inside_ul = False
                html_lines.append("</ul>")
            html_lines.append(parse_line(line))

    if inside_ul:
        html_lines.append("</ul>")


    return '\n'.join(html_lines)


def main():
    # Check is number of argument is less than 2
    if len(sys.argv) < 3:
        print(("Usage: ./markdown2html.py "
                "README.md README.html"), file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the markdown file doesn't exist
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    html_content = markdown_to_html(input_file)

    with open(output_file, 'w') as f:
        f.write(html_content)

    # If all checks pass
    sys.exit(0)

if __name__ == "__main__":
    main()
