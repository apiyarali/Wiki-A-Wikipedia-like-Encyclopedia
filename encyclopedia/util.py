import re
import random

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def markdown(entry):

    replacements=[
        (r'\r',r''), # Remove carriage retrun
        (r'(?<!\*)\*\s+(.+)',r'<li>\1</li>'), # List tag
        (r'^#{1}(?!#)\s(.+)',r'<h1>\1</h1>'), # H1 tag
        (r'^#{2}(?!#)\s(.+)',r'<h2>\1</h2>'), # H2 tag
        (r'^#{3}(?!#)\s(.+)',r'<h3>\1</h3>'), # H3 tag
        (r'^#{4}(?!#)\s(.+)',r'<h4>\1</h4>'), # H4 tag
        (r'^#{5}(?!#)\s(.+)',r'<h5>\1</h5>'), # H5 tag
        (r'^#{6}(?!#)\s(.+)',r'<h6>\1</h6>'), # H6 tag
        (r'\*\*(.+?)\*\*',r'<strong>\1</strong>'), #Strong tag
        (r'\n(?=\w)',r'\n<p>'), # P Start tag
        (r'(<p>)(.+)', r'\1\2</p>'), # P Close tag
        (r'\[(.*?)\]\((.*?)\)',r'<a href="\2">\1</a>'), #Link
        (r'((?<!\n\<\/li\>)<li>(.|\n)*?\<\/li\>(?!\n\<li\>))',r'<ul>\1</ul>'), #UL tag
        (r'\n\n',r'<br>') #Newline
    ]

    display = entry
    for pattern, substitution in replacements:
        display=re.sub(pattern,substitution,display)
    return display

def random_entry():
    entry = random.choice(list_entries())
    return entry