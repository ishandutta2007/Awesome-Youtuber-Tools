with open("README.md", "r", encoding="utf-8") as f: content = f.read()
content = content.replace('alt="Discord" /></a>', 'alt="Discord" /></a>\n  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>')
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
