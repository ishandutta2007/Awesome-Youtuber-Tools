with open("README.md", "r", encoding="utf-8") as f: content = f.read()
content = content.replace("chartrepos", "chart?repos")
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
