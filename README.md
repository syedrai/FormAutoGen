Project Description 

🚀 FormAutoGen is an automation tool built using Python + Google Forms API that dynamically creates Google Forms from JSON question files.
It’s designed to save time for educators, testers, and developers who frequently create structured question forms — such as quizzes, exams, or surveys.

⚙️ Key Features

  📄 Automatically generates Google Forms from JSON (unit1_questions.json, etc.)
  
  🔗 Instantly provides Edit and View links after creation
  
  💬 Easily customizable question templates (MCQs, short/long answers)
  
  🪄 Uses Google OAuth 2.0 authentication securely
  
  ⚡ Built with google-auth-oauthlib and googleapiclient
  
  🧰 Ideal for students, educators, and developers who manage multiple forms

🧱 Tech Stack

  Language: Python 3.10+
  
  APIs: Google Forms API, Google Drive API
  
  Libraries: google-auth-oauthlib, google-api-python-client, json
  
  Auth: OAuth 2.0 with credentials.json

🧩 Project Structure
      gender-form/
      │
      ├── create_form.py              # Main script
      ├── unit1_questions.json        # Sample input file
      ├── unit2_questions.json        # Sample input file
      ├── credentials.json            # Google OAuth credentials (not uploaded)
      └── README.md                   # Documentation

🚀 How It Works

Prepare a questions.json file with questions in structured format.

Run:

python create_form.py


Authenticate once with Google.

✅ The script will:

Create a new Google Form

Add all questions

Display “Edit” and “View” links
