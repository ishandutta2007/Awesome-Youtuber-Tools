with open("README.md", "r", encoding="utf-8") as f: content = f.read()
content = content.replace("</div>\n## 🎥", "</div>\n\n<p align=\"center\">\n  <a href=\"https://github.com/ishandutta2007/Awesome-Awesome-Awesome\"><img src=\"https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github\" alt=\"Awesome\"/></a>\n  <a href=\"https://discord.gg/jc4xtF58Ve\"><img src=\"https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white\" alt=\"Discord\" /></a>\n</p>\n## 🎥")
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
