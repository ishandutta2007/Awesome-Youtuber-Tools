with open("README.md", "r", encoding="utf-8") as f: content = f.read()
content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
