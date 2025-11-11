
```markdown
# 🤖 FormAutoGen — Google Form Automation with Python

**FormAutoGen** is a Python-based automation tool that creates Google Forms dynamically using the **Google Forms API**.  
It reads a structured `.json` question bank and automatically builds a live Google Form — complete with questions, options, and ready-to-share links.

---

## 🚀 Features

✅ Automatically creates Google Forms  
✅ Imports questions directly from JSON files  
✅ Generates both **Edit** and **View** links  
✅ Supports multiple units or topics (Unit 1, Unit 2, etc.)  
✅ Stores all generated links for future access  
✅ Clean, modular code for reuse and expansion  

---

## 🧠 Project Overview

This project was built to **save time in educational form creation**, especially for instructors, students, or training sessions where repetitive question entry wastes hours.  
By automating the process, you can upload 20–100 questions instantly to Google Forms.

---

## 📂 Folder Structure



FormAutoGen/
│
├── create_form.py
├── enrich.py
├── google_links.txt
├── questions.json
├── unit1_questions.json
├── unit2_questions.json
└── README.md



---

## 🗃️ File Descriptions

| File | Description |
|------|--------------|
| **create_form.py** | Main automation script. Handles authentication, form creation, and adding questions dynamically. |
| **enrich.py** | Pre-processing script to clean and standardize question data before uploading. |
| **google_links.txt** | Stores all generated Google Form edit & view links automatically after each run. |
| **questions.json** | Sample JSON file for testing automation on new questions. |
| **unit1_questions.json** | Question bank for Unit 1 — automatically converted into a Google Form. |
| **unit2_questions.json** | Question bank for Unit 2 — automatically converted into a Google Form. |

---
```
## 🧩 Example JSON Format
Each unit file (like `unit1_questions.json`) follows this structure:

```json
{
  "title": "Unit 1 – Cybersecurity Fundamentals",
  "description": "MCQ Practice Form for Unit 1",
  "questions": [
    {
      "question": "What does CIA stand for in Cybersecurity?",
      "options": [
        "Confidentiality, Integrity, Availability",
        "Control, Investigation, Authorization",
        "Central Internet Authority",
        "Cybersecurity Intelligence Agency"
      ]
    },
    {
      "question": "Which of the following is a type of malware?",
      "options": ["Virus", "Firewall", "Proxy", "VPN"]
    }
  ]
}
````

---

## ⚙️ Setup & Installation

### 1️⃣ Prerequisites

* Python 3.10+
* Google Cloud Project with **Forms API** and **Drive API** enabled
* `credentials.json` downloaded from Google Cloud Console

### 2️⃣ Install Dependencies

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 3️⃣ Run the Script

To create a form from your question bank:

```bash
python create_form.py
```

When prompted, authenticate with your Google account — a browser window will open for authorization.

---

## 🔗 Example Output

```
✅ Created form: 1uUneKiWsYEmUcWp0MQwC9XueJ89dIR-c8-8DjIZk7_o
✅ Added 20 questions successfully!
🔗 Edit Form: https://docs.google.com/forms/d/1uUneKiWsYEmUcWp0MQwC9XueJ89dIR-c8-8DjIZk7_o/edit
📋 View Form: https://docs.google.com/forms/d/1uUneKiWsYEmUcWp0MQwC9XueJ89dIR-c8-8DjIZk7_o/viewform
```

All generated links are also stored automatically in `google_links.txt`.

---

## 🧰 How It Works

1. `create_form.py` authenticates with Google using OAuth 2.0.
2. It reads your selected JSON file (e.g., `unit1_questions.json`).
3. A new form is created using `forms.create()` API.
4. Each question is added via a `batchUpdate` request.
5. The script prints both **Edit** and **View** links and saves them locally.

---

## 🧩 Customization

You can easily:

* Replace question banks with your own JSON data
* Add or modify units (e.g., `unit3_questions.json`)
* Enhance the design of forms via batch requests
* Integrate it with Google Sheets for automatic responses

---

## 🌐 Future Enhancements

🔹 Auto-sync results to Google Sheets
🔹 Add grading support (quiz mode)
🔹 One-click web interface with Streamlit or Flask
🔹 Add support for bulk uploads across multiple units

---

## 💻 Tech Stack

* **Language:** Python 3
* **APIs Used:** Google Forms API, Google Drive API
* **Auth:** OAuth 2.0
* **Libraries:** `google-api-python-client`, `google-auth`, `google-auth-oauthlib`

---

## 🧑‍💻 Author

**Syed Raihaan S.**
Cybersecurity Student | Developer | Automation Builder

📧 **[syedraihaan.ms@gmail.com](mailto:syedraihaan0@gmail.com)**
🌍 [LinkedIn]((https://www.linkedin.com/in/syed-raihaan-a03445291/)) | [GitHub]((https://github.com/syedrai/))

---

## 📜 License

This project is released under the **MIT License** — free to use, modify, and distribute.

> If you use this repo, please ⭐ star it on GitHub — it motivates further development!

---

### 🏁 TL;DR

> Run one script → Get a full Google Form with all your questions → Instantly shareable.
> Smart, fast, and perfect for students, teachers, and developers alike.

