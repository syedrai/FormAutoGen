import json
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes
SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive.file"
]

# Authenticate
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
creds = flow.run_local_server(port=0)
service = build("forms", "v1", credentials=creds)

# Load JSON
with open("unit1_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Step 1 — Create only the form title
form = service.forms().create(body={"info": {"title": data.get("title", "Gender Studies – MCQ Form")}}).execute()
form_id = form["formId"]
print(f"✅ Created form: {form_id}")

# Step 2 — Add description + all questions in one batchUpdate
requests = []

# Add form description
requests.append({
    "updateFormInfo": {
        "info": {
            "description": data.get("description", "MCQ Practice Form")
        },
        "updateMask": "description"
    }
})

# Add all questions
for i, q in enumerate(data["questions"]):
    requests.append({
        "createItem": {
            "item": {
                "title": q["question"],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [{"value": opt} for opt in q["options"]],
                            "shuffle": True
                        }
                    }
                }
            },
            "location": {"index": i}
        }
    })

# Send batch update
service.forms().batchUpdate(formId=form_id, body={"requests": requests}).execute()

# Step 3 — Print and open links
edit_link = f"https://docs.google.com/forms/d/{form_id}/edit"
view_link = f"https://docs.google.com/forms/d/{form_id}/viewform"

print(f"✅ Added {len(data['questions'])} questions successfully!")
print(f"🔗 Edit Form: {edit_link}")
print(f"📋 View Form: {view_link}")

# Automatically open the form in browser
webbrowser.open(edit_link)
