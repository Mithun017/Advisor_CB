import os

base = "open-source-chatbot"
structure = [
    "app.py",
    "config.py",
    "routes/chat.py",
    "services/gemini.py",
    "services/github_api.py",
    "services/memory.py",
    "requirements.txt"
]

for path in structure:
    full_path = os.path.join(base, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    open(full_path, 'a').close()

print("✅ Project structure created successfully!")
