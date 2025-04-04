# 🧠 Wiki — A Wikipedia-like Encyclopedia

This is a Django web application that emulates core functionality of Wikipedia. Users can view, search, create, edit, and explore encyclopedia entries written in Markdown, which are then rendered into HTML for display. 

**_No external markdown libraries used for converting markdown to HTML, all conversion was done via custom parsing with Regex._**

<img src="https://github.com/apiyarali/Wiki-A-Wikipedia-like-Encyclopedia/blob/07b3234928d89f00c9303a4da273f0cf8d11e3f5/screenshots/wiki_main.jpg" alt="wiki_main" width="200">

## 🔍 Features

- **Entry Pages**  
  View entries by visiting `/wiki/TITLE`. Each entry is stored in Markdown and rendered to HTML. Nonexistent entries show a custom error page.

- **Index Page**  
  The homepage lists all entries as clickable links, navigating directly to their respective pages.

- **Search**  
  - Exact match redirects to the entry.  
  - Partial matches display a list of relevant entries containing the search term.

- **Create New Entry**  
  Users can create new entries with a unique title and Markdown content. Duplicate titles are rejected with a helpful error message.
  
  <img src="https://github.com/apiyarali/Wiki-A-Wikipedia-like-Encyclopedia/blob/07b3234928d89f00c9303a4da273f0cf8d11e3f5/screenshots/wiki_newpage.jpg" alt="wiki_newpage" width="150">
  
- **Edit Entry**  
  Users can edit any existing entry. The edit form is pre-filled with the entry’s current Markdown content.

  <img src="https://github.com/apiyarali/Wiki-A-Wikipedia-like-Encyclopedia/blob/07b3234928d89f00c9303a4da273f0cf8d11e3f5/screenshots/wiki_editpage.jpg" alt="wiki_editpage" width="150">

- **Random Page**  
  Click the "Random Page" link to be taken to a randomly selected encyclopedia entry.

- **Markdown Support**  
  Markdown syntax (headings, bold, links, lists, paragraphs) is converted to HTML using a custom parser built with regular expressions.  
  **_Bonus: No external markdown libraries used!_**

## 📂 Project Structure

wiki/ ├── </br>
  &nbsp;&nbsp;├── encyclopedia/ # Main Django app │ </br> 
        &nbsp;&nbsp;&nbsp;&nbsp;├── templates/ # HTML templates │ </br>
        &nbsp;&nbsp;&nbsp;&nbsp;├── urls.py # URL routing │ </br>
        &nbsp;&nbsp;&nbsp;&nbsp;├── views.py # View logic │ </br>
        &nbsp;&nbsp;&nbsp;├── util.py # Markdown conversion & file I/O </br>
   &nbsp;&nbsp;├── entries/ # Markdown files for each entry </br>
   &nbsp;&nbsp;├── wiki/ # Project configuration </br>
   &nbsp;&nbsp;└── manage.py </br>

## 🧰 Technologies Used

- Django (Python Web Framework)
- Markdown **(custom parsing with Regex)**

    ```bash
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
    ```
  
- HTML/CSS
- Bootstrap (optional for styling)

## 📦 Setup & Installation

1. **Clone the repository**
2. **Create a virtual environment**
3. **Install dependencies** (Django)
4. **Run the server** (python manage.py runserver)
5. **Visit in browser** (Go to http://127.0.0.1:8000/)

## 💡 Markdown Syntax Supported

* Headings: #, ##, etc.
* Bold: **bold**
* Lists: * item
* Links: [text](url)
* Paragraphs and line breaks

## Future Improvements

* Add user authentication and entry history/versioning
* Support image embedding
* Add tag/categorization system
* Implement dark mode toggle

## Inspiration
Project inspired by Harvard's CS33 Web Programming curriculum.
