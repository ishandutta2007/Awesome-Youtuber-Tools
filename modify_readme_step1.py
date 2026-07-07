import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

saas_section = """| Product | Description | Pricing | Free Tier Limit | Company Size (Valuation/Revenue) |
| :--- | :--- | :--- | :--- | :--- |
| **[Final Cut Pro](https://www.apple.com/final-cut-pro/)** | Fast and intuitive editor exclusive to macOS with Magnetic Timeline and AI tools. | $299.99 one-time (Mac) / $4.99/mo (iPad) | No free tier (90-day free trial) | ~$3T Valuation |
| **[CapCut](https://www.capcut.com/)** | User-friendly mobile and desktop editor with strong AI features and TikTok/YouTube optimization. | $19.99/mo | Basic editing tools; Pro templates/effects restricted | ~$200B+ Valuation |
| **[Adobe Premiere Pro](https://www.adobe.com/products/premiere.html)** | Industry-standard video editor with powerful AI features and seamless integration with other Adobe tools. | ~$22.99/mo | No free tier (7-day free trial) | ~$87B Valuation |
| **[DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve)** | Professional-grade editor with excellent color grading, Fairlight audio, and Fusion VFX. | $295 one-time | Comprehensive tools up to 4K 60fps | ~$500M Revenue |
| **[Opus Clip](https://opus.pro/)** | AI tool that turns long videos into multiple short, viral clips optimized for YouTube and social media. | Starts at $15/mo | 60 mins/month (with watermark, expires in 3 days) | $215M Valuation |
| **[Gling.ai](https://gling.ai/)** | AI-powered editor that automatically removes silences and creates engaging YouTube videos. | Starts at $20/mo | 1 hour/month (with watermark) | <$10M Valuation |"""

old_table_regex = re.compile(r"\| Product \| Description \| Pricing \| Free Tier Limit \|\n\| :--- \| :--- \| :--- \| :--- \|\n(?:\|.*?\|\n)+", re.MULTILINE)
content = old_table_regex.sub(saas_section + "\n", content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
