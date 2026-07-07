import os

os.makedirs("assets", exist_ok=True)
svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0000ff;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)" rx="15" ry="15"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="40" font-weight="bold" fill="white">
    Awesome YouTuber Tools
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" />
  </text>
</svg>"""

with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

if "assets/banner.svg" not in content:
    content = content.replace("# Awesome-Youtuber-Tools", "# Awesome-Youtuber-Tools\n\n<div align=\"center\">\n  <img src=\"assets/banner.svg\" alt=\"Banner\" />\n</div>\n")

content = content.replace("## Top Video Editing Tools", "## 🎥 Top Video Editing Tools")
content = content.replace("## Table of Contents", "## 📋 Table of Contents")
content = content.replace("## SaaS Products", "## ☁️ SaaS Products")
content = content.replace("### Core Platforms", "### 🎯 Core Platforms")
content = content.replace("### Advanced & Specialized Platforms", "### 🚀 Advanced & Specialized Platforms")
content = content.replace("## Open-Source GitHub Projects", "## 🔓 Open-Source GitHub Projects")
content = content.replace("### Dedicated Video Editing Tools for YouTubers", "### ✂️ Dedicated Video Editing Tools for YouTubers")
content = content.replace("### Additional Strong Open-Source Options", "### 💡 Additional Strong Open-Source Options")
content = content.replace("## How to Contribute", "## 🤝 How to Contribute")
content = content.replace("## Disclaimer", "## ⚠️ Disclaimer")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
