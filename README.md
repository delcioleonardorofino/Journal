# 🧠 Technical Journal

A simple and minimalist technical journal built with **Flask**, **Jinja2**, and **Tailwind CSS**, designed to record, organize, and review software engineering learnings over time.

---

## 🚀 Features

- ✍️ Create technical journal entries
- 📚 List all logs in chronological order
- 🔍 View individual entries
- 🏷️ Organize notes by tags (e.g., backend, networking, python)
- 🎨 Clean user interface with Tailwind CSS
- ⚡ Server-side rendering with Jinja2

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- Jinja2 Templates
- Tailwind CSS
- SQLite (or another lightweight database)

---

## 📦 Installation

### 1. Clone Repo

```bash
git clone https://github.com/delcioleonardorofino/Journal.git
cd technical-journal
```

### 1. Set up a virtual environment:

```bash

   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

    Install Python dependencies:
```
```bash

   pip install -r requirements.txt

    Install and build Tailwind CSS:
```
```bash

   npm install
   npm run build:css
```
### 2. Running the Application

Start the Flask development server:

```bash

   flask run --debug
```
Watch Tailwind CSS changes (in a separate terminal):

```bash

   npm run watch:css
```
Open your browser and navigate to http://127.0.0.1:5000.
📂 Project Structure
Plain Text
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css      # Compiled Tailwind output
│   │   │   └── input.css     # Tailwind directives
│   │   └── js/
│   ├── templates/            # Jinja templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── post.html
│   ├── __init__.py
│   └── routes.py
├── posts/                    # Journal entries (Markdown or JSON)
├── tailwind.config.js
├── requirements.txt
└── run.py

### 3. 📝 Configuration (Tailwind)

The tailwind.config.js is set up to scan Jinja templates for utility classes:
JavaScript

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        background: '#09090b', // OLED/Zinc Black
        surface: '#18181b',
      }
    },
  },
  plugins: [],
}
```

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
