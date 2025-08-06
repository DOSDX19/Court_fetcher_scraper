# 🏛️ Court-Data Fetcher & Mini-Dashboard (Delhi High Court)

A Django + Selenium web app that allows users to fetch case metadata from the Delhi High Court public portal using case type, number, and filing year.

---

## 🚀 Features

- Input form for: **Case Type**, **Case Number**, and **Filing Year**
- Selenium automation to submit the form on [https://delhihighcourt.nic.in/case.asp](https://delhihighcourt.nic.in/case.asp)
- Extracts:
  - Party names
  - Filing date
  - Next hearing date
  - Latest order/judgment PDF link
- Stores each query and raw HTML in **SQLite**
- Displays results cleanly in the browser

---

## 🖥️ Live Preview

> Run locally and access: `http://127.0.0.1:8000/`

---

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Scraping**: Selenium (headless browser automation)
- **Database**: SQLite
- **Frontend**: HTML (Django templates)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/court-data-fetcher.git
cd court-data-fetcher
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Download & install ChromeDriver

- Go to: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
- Download the version that matches your Chrome
- Place it in your project directory or system PATH

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

---

## 🧪 Example Input

| Field         | Example   |
|---------------|-----------|
| Case Type     | W.P.(C)   |
| Case Number   | 12345     |
| Filing Year   | 2023      |

---

## ❗ Known Limitations

- CAPTCHA on the Delhi High Court site may block scraping intermittently.
- This version does not bypass CAPTCHA (future work could integrate external solvers).

---

## 📁 Project Structure

```
court_data_fetcher/
├── court_fetcher/
├── scraper/
│   ├── views.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── templates/
│       └── form.html
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📚 License

MIT License — Free to use, modify, and distribute.

---

## 👤 Author

**Ahmed Qureshi**  
[LinkedIn](https://www.linkedin.com/in/ahmed-qureshi-dev) | [GitHub](https://github.com/your-username)

---

## 🙏 Contributions & Feedback

Pull requests are welcome.  
Feel free to open issues or suggest improvements!
